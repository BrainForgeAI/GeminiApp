import React from 'react';

function Questions({ faq, index, toggleFAQ }) {
  return (
    <div className={"faq " + (faq.open ? 'open' : '')} key={index}>
      <div className="faq-question" onClick={() => toggleFAQ(index)}>
        {faq.question}
      </div>
      {faq.open && (
        <div className="faq-answer">
          {faq.answer}
        </div>
      )}
    </div>
  );
}

export default Questions;
