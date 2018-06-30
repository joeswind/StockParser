import React from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

const divStyle = {
  color: 'red'
};

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }
  render() {
    return (
      <div style={divStyle}>Hello World!</div>
    );
  }
}

// const 為常數
const lists = ['JavaScript', 'Java', 'Node', 'Python'];

class HelloMessage extends React.Component {
  render() {
    return (
    <ul>
      {lists.map((result, index) => {
        return (<li key={index}>{result}</li>);
      })}
    </ul>);
  }
}

//  注意元件開頭第一個字母都要大寫
class MyComponent extends React.Component {
	// render 是 Class based 元件唯一必須的方法（method）
	render() {
		return (
			<div>Hello, {this.props.name}</div>
		);
	}
}

// PropTypes 驗證，若傳入的 props type 不符合將會顯示錯誤
MyComponent.propTypes = {
	name: PropTypes.string
}

// Prop 預設值，若對應 props 沒傳入值將會使用 default 值，為每個實例化 Component 共用的值
MyComponent.defaultProps = {
 	name: 'Al',
}


class LifeCycleComponent extends React.Component {
  constructor(props) {
    super(props);
    console.log('constructor');
    this.handleClick = this.handleClick.bind(this);
    this.state = {
      name: 'Mark',
    }
  }
  handleClick() {
    this.setState({'name': 'Zuck'});
  }
  componentWillMount() {
    console.log('componentWillMount');
  }
  componentDidMount() {
    console.log('componentDidMount');
  }
  componentWillReceiveProps() {
    console.log('componentWillReceiveProps');
  }
  componentWillUpdate() {
    console.log('componentWillUpdate');
  }
  componentDidUpdate() {
    console.log('componentDidUpdate');
  }
  componentWillUnmount() {
    console.log('componentWillUnmount');
  }
  render() {
    return (
      <div onClick={this.handleClick}>Hi, {this.state.name}</div>
    );
  }
}

ReactDOM.render(<LifeCycleComponent />, document.getElementById('app'));

//ReactDOM.render(<MyComponent name="Hank" />, document.getElementById('app'));