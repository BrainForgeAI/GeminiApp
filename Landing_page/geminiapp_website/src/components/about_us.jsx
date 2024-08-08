import React from "react";
import "../styles/about.css";

const About = () => {
  return (
    <div className="About_background">
      <div className="about-container">
        <h1 className="main-title">
          Learning can be hard. We can change that.
        </h1>

        <div className="content">
          <p>
            Our team at EduQuest is driven by a singular mission: to ignite the
            spark of learning in every individual, regardless of age or
            background. With the emergence of advanced AI technologies,
            particularly Google's Multimodal Gemini Model, we've unlocked the
            potential to provide each student with a personalized, expert tutor
            across a vast array of subjects. This groundbreaking approach allows
            us to dynamically adapt to each learner's unique needs, pace, and
            interests.
          </p>

          <p>
            By combining cutting-edge AI into an engaging gaming format, we
            create an immersive learning environment where education feels less
            like a chore and more like an exciting adventure. Our adaptive
            platform continuously assesses each student's progress, adjusting
            the difficulty and content in real-time to ensure optimal challenge
            and growth. Whether a student is struggling with basic concepts or
            ready for advanced material, our AI-powered system tailors the
            experience to keep them motivated and progressing.
          </p>
        </div>

        <h2 className="section-title">Our Story</h2>

        <div className="content">
          <p>
            The beauty of our approach lies in its ability to transform learning
            into play while accommodating diverse learning styles. As students
            navigate through captivating quests and solve intriguing puzzles,
            they're simultaneously mastering crucial skills and knowledge at
            their own pace. For students with learning disabilities, we
            incorporate specialized tools and strategies, to ensure every
            learner can access and engage with the material effectively.
          </p>

          {/* Add the rest of the paragraphs here */}
        </div>
        {/* 
      <h2 className="cta-title">Interested? What are you waiting for?</h2>
      <button className="cta-button">PLAY NOW</button> */}
      </div>
    </div>
  );
};

export default About;
