import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./styles/App.css";
import Navbar from "./components/navbar.jsx";
import Homepage from "./components/home.jsx";
import About from "./components/about_us.jsx";
import Gallery from "./components/gallery.jsx";
import FAQ from "./components/FAQ.jsx";
import Contact from "./components/contact.jsx";
import SplashScreen from "./splashscreen.jsx";
import Demo from "./components/demo.jsx";
import "./styles/styles.css";

function App() {
  const [isBooting, setSplash] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setSplash(false);
    }, 4000);
  }, []);
  if (isBooting) {
    return <SplashScreen />;
  }

  return (
    <Router>
      <div className="App">
        {isBooting ? (
          <SplashScreen />
        ) : (
          <>
            <Navbar />
            <Routes>
              <Route path="/" element={<Homepage />} />
              <Route path="/about" element={<About />} />
              <Route path="/gallery" element={<Gallery />} />
              <Route path="/contact" element={<Contact />} />
              <Route path="/faq" element={<FAQ />} />
              <Route path="/demo" element={<Demo />} /> 
            </Routes>
          </>
        )}
      </div>
    </Router>
  );
}

export default App;
