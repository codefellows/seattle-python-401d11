import React, { Component } from 'react';
import './App.css';
import Landing from './landing/Landing';
import Main from './main/Main';

class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
      token: ''
    }
    this.onLogin = this.onLogin.bind(this);
  }

  onLogin(token) {
    this.setState({
      token
    })
  }

  render() {

    return (
      <div className="App">
      {this.state.token ?
        <Main token={this.state.token} />
        :
        <Landing onLogin={this.onLogin} />
      }
      </div>
    );
  }
}

export default App;
