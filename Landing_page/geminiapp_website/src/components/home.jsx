import React from "react";
import { Link } from "react-router-dom";
import backgroundImage from "../Assets/background.png";
import "../styles/home.css";
import heroLogo from "../Assets/hero_logo.png";
import ctaImage from "../Assets/CTA-img.png";
import galleryIslands from "../Assets/gallery_frame.png";
import Footer from "./footer";


const Homepage = () => {
  return (
    <body>
      <section className="section-hero">
        <div className="hero-content">
          <img className="hero-logo" src={heroLogo} alt="Hero Logo" />
          <a href="#section-gallery" className="learn-more-btn">
            Learn More
          </a>
        </div>
      </section>

      <section className="section-gallery" id="section-gallery">
        <div className="container">
          <p>
            EduQuest harnesses <span>G</span>
            <span>o</span>
            <span>o</span>
            <span>g</span>
            <span>l</span>
            <span>e</span>
            <span>'</span>
            <span>s</span> Gemini AI Model to revolutionize learning. Our
            adaptive platform creates personalized game-like experiences,
            tailoring challenges to each user's pace and style.
          </p>
          <div className="video-box">
            <iframe
              width="560"
              height="315"
              src="https://www.youtube.com/embed/AKQTWVEM-Xo?si=Zu95CqAIO-Ji10_Z"
              title="YouTube video player"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </div>
        </div>
        <img
          className="gallery-islands"
          src={galleryIslands}
          alt="Pixel art islands"
        />
      </section>

      <section className="section-CTA">
        <div className="container">
          <div className="CTA-content">
            <h1>
              PLAY <span>SMART.</span> GROW <span>SMARTER.</span>
            </h1>
            <p>
              EduQuest harnesses Google's Gemini AI Model to revolutionize
              learning. Our adaptive platform creates personalized game-like
              experiences, tailoring challenges to each user's pace and style.
              We make education engaging and accessible for everyone. The joy of
              learning is something everyone deserves to experience.
            </p>
          </div>
          <div className="CTA-box">
            <img
              className="CTA-gameboy-img"
              src={ctaImage}
              alt="Handheld gaming device"
            />
            <Link to="/demo" className="full-rounded">
              PLAY DEMO
            </Link>
          </div>
        </div>
      </section>
      <Footer/>
    </body>
    
  );
};

export default Homepage;
