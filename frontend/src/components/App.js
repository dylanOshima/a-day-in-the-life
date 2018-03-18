import React, { Component } from 'react';
import Nav from './Nav';
import Videos from './Videos';
import '../styles/App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Nav />
        <Videos />
      </div>
    );
  }
}

export default App;
