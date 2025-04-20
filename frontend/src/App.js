import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Signup from './Signup';
import Dashboard from './Dashboard';

function App() {
  return (
    <div className="App">
      <h1>My React App</h1>
      <Dashboard />
    </div>
  );
}


export default App;
