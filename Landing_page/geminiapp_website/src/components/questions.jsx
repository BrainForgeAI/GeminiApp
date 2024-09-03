import React from 'react'

function questions(faq, i) {
  return (
    <div 
        className={"faq " + (faq.open ? 'open' : '')}
        key={i}
    >
        <div className="faq-question">
            {faq.question}
        </div>
        <div className="faq-answer">
            {faq.answer}
        </div>
    </div>
  )
}

export default questions
