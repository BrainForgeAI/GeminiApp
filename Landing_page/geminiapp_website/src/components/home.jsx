import React from "react";
import { Link } from "react-router-dom";
import backgroundImage from "../Assets/background.png";
import "../styles/home.css";

const Homepage = () => {
  return (
    <body
    // className="full-page-background"
    // style={{ backgroundImage: url(${backgroundImage}) }}
    >
      <div className="container">
        <section className="section-hero">
          <img
            className="hero-logo"
            src="../Assets/hero_logo.png"
            alt="Hero Logo"
          ></img>
          {/* ^ This is not working for some reason */}

          <a href="#section-gallery" className="learn-more-btn">
            Learn More
          </a>
        </section>
        <section className="section-gallery" id="section-gallery">
          <p>
            EduQuest harnesses Google’s Gemini AI Model to revolutionize
            learning. Our adaptive platform creates personalized game-like
            experiences, tailoring challenges to each user's pace and style.
          </p>
        </section>
        <section className="hero">
          <h1>
            PLAY <span>SMART.</span> GROW <span>SMARTER.</span>
          </h1>
          <p className="quick-intro">
            EduQuest harnesses Google's Gemini AI Model to revolutionize
            learning. Our adaptive platform creates personalized game-like
            experiences, tailoring challenges to each user's pace and style. We
            make education engaging and accessible for everyone. The joy of
            learning is something everyone deserves to experience
          </p>
        </section>

        <section>
          <div className="video-box">
            <iframe
              width="560"
              height="315"
              src="https://www.youtube.com/embed/PLUhJmqHd1s"
              title="YouTube video player"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </div>
        </section>

        <Link to="/demo" className="full-rounded play-now-button">
          PLAY DEMO
        </Link>
        
        {/* <button className="download-button">LEARN MORE</button> */}
      </div>
    </body>
  );
};

export default Homepage;
