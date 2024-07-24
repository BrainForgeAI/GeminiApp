import React from 'react';
import './App.css';
import Navbar from './components/navbar.jsx';
import Homepage from './components/how_it_works.jsx';
import './navbar.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Homepage />
    </div>
  );
}

export default App;