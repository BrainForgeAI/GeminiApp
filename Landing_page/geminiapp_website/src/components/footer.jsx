import React from "react";
import { Link } from "react-router-dom";
import "../styles/footer.css";

const Footer = () => {
  return (
    <section className="section-footer">
      <div className="footer-left">
        <span className="brand-name">BRAINFORGE</span>
        <span className="brand-bio">A smart way to learn</span>
      </div>
      <div className="footer-mid">
        <span>Get up to date on the latest updates</span>
        <span>MAYBE EMAIL BOX HERE</span>
      </div>
      <div className="footer-right">
        <span>Follow us</span>
        <a href="https://www.linkedin.com/" target="_blank">
          LinkedIn
        </a>
        <a href="https://www.github.com/" target="_blank">
          Github
        </a>
      </div>
    </section>
  );
};

export default Footer;
