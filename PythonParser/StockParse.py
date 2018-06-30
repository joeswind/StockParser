import requests
from io import StringIO
import pandas as pd
import numpy as np

datestr = '20180131'

r = requests.post('http://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALL')

afterProcessStr = StringIO("\n".join(
        [
            i.translate({ord(c): None for c in ' '}) 
            for i in r.text.split('\n') 
                if len(i.split('",')) == 17 and i[0] != '='
        ])
    )

df = pd.read_csv(afterProcessStr, header=0)

print(afterProcessStr.getvalue())
print(datestr)