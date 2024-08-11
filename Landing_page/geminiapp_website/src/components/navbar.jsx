import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "../styles/navbar.css";

const Navbar = () => {
  const [scrollDirection, setScrollDirection] = useState("top");

  useEffect(() => {
    let lastScrollTop = 0;
    const handleScroll = () => {
      const currentScroll = window.scrollY;
      if (currentScroll > lastScrollTop) {
        setScrollDirection("down");
      } else {
        setScrollDirection("up");
      }
      if (currentScroll === 0) {
        setScrollDirection("top");
      }
      lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <nav className={`navbar ${scrollDirection}`}>
      <div className="navbar-left">
        <span className="brand-name">BRAINFORGE</span>
        {/* replace with a logo */}
      </div>
      <div className="navbar-center">
        <Link to="/">HOME</Link>
        <Link to="/about">ABOUT</Link>
        <Link to="/gallery">GALLERY</Link>
        <Link to="/faq">FAQ</Link>
        <Link to="/contact">CONTACT</Link>
      </div>
      <div className="navbar-right">
        <a className="signup-btn">SIGN-UP</a>
        {/* <button className="signup-button">SIGN UP</button> */}
      </div>
    </nav>
  );
};

export default Navbar;
