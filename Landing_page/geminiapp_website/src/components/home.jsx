import React from "react";
import { Link } from "react-router-dom";
import backgroundImage from "../Assets/background.png";
import "../styles/home.css";

const Homepage = () => {
  return (
    <body>
      <div className="container">
        <section className="section-hero">
          <div className="hero-content">
            <img
              className="hero-logo"
              src={require("../Assets/hero_logo.png")}
              alt="Hero Logo"
            ></img>
            {/* ^ This is not working for some reason */}

            <a href="#section-gallery" className="learn-more-btn">
              Learn More
            </a>
          </div>
        </section>
        <section className="section-gallery" id="section-gallery">
          <p>
            EduQuest harnesses Google's Gemini AI Model to revolutionize
            learning. Our adaptive platform creates personalized game-like
            experiences, tailoring challenges to each user's pace and style.
          </p>
          {/* <img
            className="gallery-img"
            src={require("../Assets/gallery-hero.png")}
            alt="Image of game frame"
          /> */}
          <div className="video-box">
            <iframe
              width="560"
              height="315"
              src="https://www.youtube.com/embed/IBP5NUDP28A?si=FXJjmZIJ63ruJ_F5"
              title="YouTube video player"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </div>
        </section>
        <section className="section-CTA">
          <div className="CTA-content">
            <h1>
              PLAY <span>SMART.</span> GROW <span>SMARTER.</span>
            </h1>
            <p>
              EduQuest harnesses Google's Gemini AI Model to revolutionize
              learning. Our adaptive platform creates personalized game-like
              experiences, tailoring challenges to each user's pace and style.
              We make education engaging and accessible for everyone. The joy of
              learning is something everyone deserves to experience
            </p>
            <img
              className="CTA-text-img"
              src={require("../Assets/strategy_and_innovation.png")}
              alt="Strategy and innovation"
            />
            <Link to="/demo" className="full-rounded play-now-button">
              PLAY DEMO
            </Link>
          </div>
          <img
            className="CTA-gameboy-img"
            src={require("../Assets/gameboy.png")}
            alt="Image of handheld gaming device with game popping out"
          />
        </section>
        {/* <section>
          <div className="video-box">
            <iframe
              width="560"
              height="315"
              src="https://www.youtube.com/embed/IBP5NUDP28A?si=FXJjmZIJ63ruJ_F5"
              title="YouTube video player"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </div>
        </section> */}
      </div>
    </body>
  );
};

export default Homepage;
