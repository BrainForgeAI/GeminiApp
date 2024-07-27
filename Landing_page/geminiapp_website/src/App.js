import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Navbar from './components/navbar.jsx';
import Homepage from './components/home.jsx';
import About from './components/about_us.jsx';
import Gallery from './components/gallery.jsx'; // Capitalize component name
import './navbar.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/about" element={<About />} />
          <Route path="/gallery" element={<Gallery />} /> 
        </Routes>
      </div>
    </Router>
  );
}

export default App;