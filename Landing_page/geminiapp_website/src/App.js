import React from 'react';
import './App.css';
import Navbar from './components/navbar.jsx';
import HowItWorks from './components/how_it_works.jsx';
import './navbar.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <HowItWorks />
    </div>
  );
}

export default App;