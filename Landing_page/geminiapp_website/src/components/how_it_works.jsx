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

            <div className="card-content">
              <h3 className="card-title">GAME BOX</h3>
            </div>
          </div>
          {/* Add more cards as needed */}
        </div>
      </section>
    </div>
  );
};

export default HowItWorks;