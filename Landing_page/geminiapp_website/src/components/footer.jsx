import React from "react";
import { Link } from "react-router-dom";
import "../styles/footer.css";
import { IonIcon } from "@ionic/react";
import { logoGithub } from "ionicons/icons";
import { logoLinkedin } from "ionicons/icons";

const Footer = () => {
  return (
    <section className="section-footer">
      <div className="footer-left">
        <p>
          <span className="copyright">&copy;2024</span> BRAINFORGE
        </p>
      </div>
      <div className="footer-mid">
        <img
          className="logo-img"
          src={require("../Assets/final_logo.png")}
          alt="BrainForge Logo"
        />
      </div>
      <div className="footer-right">
        <a
          className="footer-link"
          href="https://www.linkedin.com/company/brainforge-ai/about/"
          target="_blank"
        >
          <IonIcon icon={logoLinkedin}></IonIcon>
        </a>
        <a
          className="footer-link"
          href="https://github.com/BrainForgeAI"
          target="_blank"
        >
          <IonIcon icon={logoGithub}></IonIcon>
        </a>
      </div>
    </section>
  );
};

export default Footer;
