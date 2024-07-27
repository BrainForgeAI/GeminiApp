import React from 'react';
import backgroundImage from '../Assets/background.png'

const Homepage = () => {
  return (
    <div className="full-page-background" style={{ backgroundImage: `url(${backgroundImage})` }}>
      <div className="container">
        <section className="hero">
          <h1>PLAY <span>SMART.</span> GROW <span>SMARTER.</span></h1>
          <p className="quick-intro">EduQuest harnesses Google's Gemini AI Model to revolutionize learning. Our adaptive platform creates personalized game-like experiences, 
            tailoring challenges to each user's pace and style. We make education engaging and accessible for everyone. The joy of learning is something everyone deserves to experience</p>
        </section>

        <section>
            <div className="video-box">
            <iframe
            width="560" 
            height="315"
            src="https://www.youtube.com/embed/PLUhJmqHd1s" 
            title="YouTube video player"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen>
          </iframe>
            </div>
        </section>
        <button className="download-button">LEARN MORE</button>   
      </div>
    </div>
  );
};

export default Homepage;