import React from 'react'
import BrainForgeLogo from '../Assets/Brainforge_Logo.png'
import { Link } from "react-router-dom";
import "../styles/navbar.css";

const navbar = () => {
  return (
    <div className='Navbar Shelf'>

<div className = 'Logo-Container'>
        <img src={BrainForgeLogo} alt = ""/>
      </div>

      <div className='NavBar-Links-Container'>
        <Link to="/">HOME</Link>
        <Link to="/about">ABOUT</Link>
        <Link to="/gallery">GALLERY</Link>
        <Link to="/faq">FAQ</Link>
        <Link to="/contact">CONTACT</Link>
        <button className='SignIn_Button'>Sign In</button>
      </div>




    </div>
  )
}

export default navbar