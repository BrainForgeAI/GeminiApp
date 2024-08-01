import React from 'react';
import './splashscreen.css';
import Icon from './Assets/icon.png';

const SplashScreen = () => {
  return (
    <div className="splash">
      <img src={Icon} alt="Loading Logo" />
    </div>
  );
}

export default SplashScreen;
