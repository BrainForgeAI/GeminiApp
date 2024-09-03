import React, { useState } from "react";
import "../styles/faq.css";
import Questions from './questions.jsx';

const FAQ = () => {
  const [faqs, setFaqs] = useState([
    {
      question: 'Does Aspectus have controller support?',
      answer: 'Currently, Aspectus does not have controller support on PC.',
      open: false
    },
    {
      question: 'What subjects does Aspectus support?',
      answer: 'Anything! Seriously, any subject. Since the game uses Google’s Gemini AI to generate personalized, relevant questions, the possibilities are endless. Whether it’s grade school math, astronomy, or WWII history, Aspectus can handle it all—just upload your course notes and let the game do the rest!',
      open: false
    },
    {
      question: 'Can you play the game in co-op or multiplayer?',
      answer: 'No, Aspectus is currently a single-player experience. While there are no plans for multiplayer at the moment, the team is exploring this as a potential feature in future updates.',
      open: false
    },
    {
      question: 'What language was Aspectus coded in?',
      answer: 'Aspectus was developed in C# using the Unity engine. It features a unique storyline and stunning original artwork, all crafted from the ground up.',
      open: false
    },
    {
      question: 'Can I upload notes in any format?',
      answer: 'At the moment, Aspectus only supports PDF-formatted course notes. We plan to add support for other file formats in the future, but for now, the game is optimized to work with PDFs only.',
      open: false
    },
    {
      question: 'Can I use Aspectus to teach my dog quantum physics?',
      answer: "While Aspectus is a powerful learning tool, we're not quite sure your dog will grasp quantum mechanics (yet). But hey, feel free to give it a try—just don't expect them to start solving Schrödinger's equation anytime soon!",
      open: false
    },
    {
      question: 'Will Aspectus do my homework for me??',
      answer: "As much as we'd love to help, Aspectus is here to teach you, not do your homework! But with the right questions and practice, you'll be acing your assignments in no time—no shortcuts allowed!",
      open: false
    },
    ]);

  const toggleFAQ = (index) => {
    setFaqs(
      faqs.map((faq, i) => 
        i === index ? { ...faq, open: !faq.open } : faq
      )
    );
  };

  return (
    <div className="FAQ">
      {faqs.map((faq, i) => (
        <Questions faq={faq} index={i} key={i} toggleFAQ={toggleFAQ} />
      ))}
    </div>
  );
}

export default FAQ;
