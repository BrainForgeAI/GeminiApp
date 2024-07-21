import React from 'react'

const navbar = () => {
  return (
    <nav className="navbar">
    <div className="navbar-left">
    <span className="brand-name">EDUQUEST</span>
    </div>
    <div className="navbar-center">
      <a href="how-it-works">HOW IT WORKS</a>
      <a href="about-us">ABOUT US</a>
    </div>
    <div className="navbar-right">
      <button className="play-button">PLAY</button>
    </div>
  </nav>
  )
}

export default navbar