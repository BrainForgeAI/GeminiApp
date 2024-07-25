import React from 'react';

const HowItWorks = () => {
  return (
    <div className="container">
      <section className="hero">
        <h1>PLAY <span>SMART.</span> GROW <span>SMARTER.</span></h1>
        <p className="quick-intro">EduQuest harnesses Google’s Gemini AI Model to revolutionize learning. Our adaptive platform creates personalized game-like experiences, 
          tailoring challenges to each user's pace and style. We make education engaging and accessible for everyone. The joy of learning is something everyone deserves to experience</p>
      </section>

      <section>
      <button className="download-button">DOWNLOAD NOW</button> 
        <div className="card-grid">
          <div className="card">

            {/* <div className="card-content"> */}
              {/* <h3 className="card-title">GAME BOX</h3> */}
            {/* </div> */}
          </div>
          {/* Add more cards as needed */}
        </div>
      </section>
    </div>
  );
};

export default HowItWorks;