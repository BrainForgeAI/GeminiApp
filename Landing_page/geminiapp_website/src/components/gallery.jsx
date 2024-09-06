import React, { useState } from 'react';
import '../styles/gallery.css'; // Import the CSS file
import Image1 from '../Assets/GallaryImage1.png';
import Image2 from '../Assets/GallaryImage2.png';
import Footer from "./footer";


const images = [
  Image1,
  Image2
];

const Gallery = () => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const goToPrevious = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0 ? images.length - 1 : prevIndex - 1
    );
  };

  const goToNext = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === images.length - 1 ? 0 : prevIndex + 1
    );
  };

  return (
    <div className="fullscreen-background">
       <div className="top-gradient"></div>
    {/* Gallery container */}
    <div className="gallery-container">
      <button
        onClick={goToPrevious}
        className="gallery-button gallery-button-left"
      >
        &#10094;
      </button>

      <img
        src={images[currentIndex]}
        alt="Gallery"
        className="gallery-image"
      />

      <button
        onClick={goToNext}
        className="gallery-button gallery-button-right"
      >
        &#10095;
      </button>
    </div>
    </div>
  );
};

export default Gallery;