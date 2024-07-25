import React from 'react'

const navbar = () => {
  return (
    <nav className="navbar">
    <div className="navbar-left">
    <span className="brand-name">EDUQUEST</span>
    </div>
    <div className="navbar-center">
      <a href="home">HOME</a>
      <a href="about">ABOUT</a>
      <a href="gallery">GALLERY</a>
      <a href="faq">FAQ</a>
      <a href="contact">CONTACT</a>

    </div>
    <div className="navbar-right">
      <button className="signup-button">SIGN UP</button>  
    </div>
  </nav>
  )
}

export default navbar