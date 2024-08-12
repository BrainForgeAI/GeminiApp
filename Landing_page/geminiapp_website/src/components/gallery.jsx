import React, {useState} from "react";
import "../styles/gallery.css";
import Masonry, {ResponsiveMasonry} from "react-responsive-masonry";

import gameui from "../Assets/Gallery/gameui.png";
import dialogue from "../Assets/Gallery/dialogue.png";
import characterModel from "../Assets/Gallery/character-model.png";
import elderguyWithCane from "../Assets/Gallery/elderguywithcane.png";
import firstNpc from "../Assets/Gallery/first-npc.png";
import guardModel from "../Assets/Gallery/guard-model.png";

const images = [
  gameui,
  dialogue,
  characterModel,
  elderguyWithCane,
  firstNpc,
  guardModel,
];

const Gallery = () => {
  const [data, setData] = useState({img: '', i: 0})

  const viewPhoto = (img, i)=>{
      setData({img, i})
  }

  const buttonCommand = (command) =>{
    let i = data.i;
    if (command === 'next-img'){
      setData({img: images[i + 1], i: i + 1});
    }
    if (command === 'prev-img'){
      setData({img: images[i - 1], i: i - 1});
    }
    if (!command){
      setData({img: '', i: 0});
    }
  }

  return (
    <>
      {data.img &&
        <div style={{
            width: '100%',
            height: '100vh',
            background: 'black',
            position: 'fixed',
            display: 'center',
            justifyContent: 'center',
            alignItems: 'center',
            overflow: 'hidden',
        }}>
          <button className="gallery-btn" onClick={() => buttonCommand()} style={{position: 'absolute', top: '10px', right: '10px'}}>
            Exit
          </button>
          <button className="gallery-btn" onClick={()=> buttonCommand('prev-img')}>Previous</button>
          <img src = {data.img} style = {{width: 'auto', maxWidth: '85%', maxHeight: '85%'}} />
          <button className="gallery-btn" onClick={() => buttonCommand('next-img')}>Next</button>
        </div>
      }
      <div style={{padding: '12px'}}>
        <Masonry columnsCount={2} gutter="15px">
          {images.map((image, i) => (
            <img
              key={i}
              src={image}
              style={{width: "100%", display: "block", cursor: 'pointer'}}
              onClick={()=>viewPhoto(image, i)}
            />
          ))}
        </Masonry>
      </div>
    </>
  );
};

export default Gallery;
