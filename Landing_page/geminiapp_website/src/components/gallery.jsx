import React, { useState, useEffect} from "react";
import "../styles/gallery.css";
import Masonry from "react-responsive-masonry";

// Import images
import gameui from "../Assets/Gallery/gameui.png";
import dialogue from "../Assets/Gallery/dialogue.png";
import characterModel from "../Assets/Gallery/character-model.png";
import elderguyWithCane from "../Assets/Gallery/elderguywithcane.png";
import firstNpc from "../Assets/Gallery/first-npc.png";
import guardModel from "../Assets/Gallery/guard-model.png";
import titlescreen from "../Assets/Gallery/titlescreen.png";
import villagerDialogue from "../Assets/Gallery/villager-dialogue.png";

const images = [
  gameui,
  dialogue,
  characterModel,
  elderguyWithCane,
  firstNpc,
  guardModel,
  titlescreen,
  villagerDialogue,
];

const Gallery = () => {
  const [data, setData] = useState({ img: '', i: 0 });
  
  const viewPhoto = (img, i) => {
    setData({ img, i });
  };

  const buttonCommand = (command) => {
    let i = data.i;
    if (command === 'next-img' && i < images.length - 1) {
      setData({ img: images[i + 1], i: i + 1 });
    }
    if (command === 'prev-img' && i > 0) {
      setData({ img: images[i - 1], i: i - 1 });
    }
    if (!command) {
      setData({ img: '', i: 0 });
    }
  };

  return (
    <div className="background-container">
      {data.img && (
        <div
          style={{
            width: '100%',
            height: '100vh',
            background: 'black',
            position: 'fixed',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            overflow: 'hidden',
          }}
        >
          <button
            className="gallery-btn"
            onClick={() => buttonCommand()}
            style={{ position: 'absolute', top: '100px', right: '10px' }}
          >
            Exit
          </button>
          <button className="gallery-btn" onClick={() => buttonCommand('prev-img')}>
            Previous
          </button>
          <img
            src={data.img}
            style={{ width: 'auto', maxWidth: '85%', maxHeight: '85%' }}
            alt="Selected"
          />
          <button className="gallery-btn" onClick={() => buttonCommand('next-img')}>
            Next
          </button>
        </div>
      )}
      <div style={{ padding: '10px' }}>
        <Masonry columnsCount={3} gutter="20px">
          {images.map((image, i) => (
            <img
              key={i}
              src={image}
              style={{ width: '100%', display: 'block', cursor: 'pointer' }}
              onClick={() => viewPhoto(image, i)}
              alt={`Gallery image ${i}`}
            />
          ))}
        </Masonry>
      </div>
    </div>
  );
};

export default Gallery;
