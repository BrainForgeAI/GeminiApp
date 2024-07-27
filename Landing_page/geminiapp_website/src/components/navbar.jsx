import React from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <span className="brand-name">BRAINFORGE</span>
      </div>
      <div className="navbar-center">
        <Link to="/">HOME</Link>
        <Link to="/about">ABOUT</Link>
        <Link to="/gallery">GALLERY</Link>
        <Link to="/gallery">FAQ</Link>
        <Link to="/gallery">CONTACT</Link>
      </div>
      <div className="navbar-right">
        <button className="signup-button">SIGN UP</button>  
      </div>
    </nav>
  )
}

export default Navbar