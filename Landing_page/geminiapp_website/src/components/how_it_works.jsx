import React from 'react';

const HowItWorks = () => {
  return (
    <div className="container">
      <section className="hero">
        <h1>CREATE YOUR <span>UNIVERSE</span>.</h1>
        <p>Interactive fan experiences in the worlds of your favorite books, movies, and TV shows. Play, share, and remix with your friends.</p>
      </section>

      <section>
        <h2 className="section-title">PLAY IN THE WORLD OF...</h2>
        <div className="card-grid">
          <div className="card">
            <img src="/path-to-image/pride-and-prejudice.jpg" alt="Pride and Prejudice" className="card-image" />
            <div className="card-content">
              <h3 className="card-title">PRIDE AND PREJUDICE</h3>
              <p>by Jane Austen</p>
              <div className="card-tags">
                <span className="tag">Romance</span>
                <span className="tag">Classics</span>
              </div>
              <a href="#read-more" className="card-cta">READ MORE</a>
            </div>
          </div>
          {/* Add more cards as needed */}
        </div>
      </section>
    </div>
  );
};

export default HowItWorks;