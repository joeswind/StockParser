import requests
from io import StringIO
import pandas as pd
import numpy as np
import pymongo
import json
import datetime

datestr = datetime.datetime.now().strftime('%Y%m%d')

myclient = pymongo.MongoClient('35.234.46.106:27017', username='tsUser', password='1qaz@WSX', authSource='TaiwanStock', authMechanism='SCRAM-SHA-1')
twStockDB = myclient["TaiwanStock"]
stockDateInfos = twStockDB["StockDateInfos"]
parseLog = twStockDB["ParseLog"]

r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')

# 首先判斷是否有傳回來的值
if(r.text == ''):
    print('no data')
else:
    parseCount = parseLog.find({'ParseType': 'StockDateInfos', 'Date': datestr}).count()
    if(parseCount > 0):
        stockDateInfos.delete_many({ 'date': datestr })
        parseLog.update_one({'ParseType': 'StockDateInfos', 'Date': datestr}, { '$set': { 'ParseTime': datetime.datetime.now() } }, upsert=False)
    else:
        parseLog.insert_one({ 'ParseType': 'StockDateInfos', 'Date': datestr, 'ParseTime': datetime.datetime.now() })
    

    # 處理取下來的csv資料
    afterProcessStr = StringIO("\n".join(
            [
                i.translate({ord(c): None for c in ' '}) 
                for i in r.text.split('\n') 
                    if len(i.split('",')) == 17 and i[0] != '='
            ])
        )
    df = pd.read_csv(afterProcessStr, header=0)
    jsonStr = df.to_json(orient='records')
    stockInfos = json.loads(jsonStr)
    for stock in stockInfos:
        stock['date'] = datestr
    stockDateInfos.insert_many(stockInfos)
    print(datestr + ' Parse Finish')

    # 顯示解析出來的JSON STRING
    #print(jsonStr)