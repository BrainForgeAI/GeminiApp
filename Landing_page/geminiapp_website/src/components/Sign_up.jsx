import React, { useState } from "react";
import "../styles/signup.css";
import {
  Container,
  TextField,
  Button,
  Typography,
  Box,
  Link,
} from "@mui/material";

const SignupPage = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log("Form Data:", formData);
  };

  return (
    <body>
      <section className="section-signup">
        <div className="form-box">
          <form onSubmit={handleSubmit}>
            <div className="form-subbox">
              <label className="form-label" for="fname">
                Name
              </label>
              <input
                className="form-input"
                type="text"
                id="fname"
                placeholder="John Doe"
              ></input>
            </div>
            <div className="form-subbox">
              <label className="form-label" for="femail">
                Email
              </label>
              <input
                className="form-input"
                type="text"
                id="femail"
                placeholder="JohnDoe@email.com"
              ></input>
            </div>
            <div className="form-subbox">
              <button>Sign Up</button>
            </div>
          </form>
        </div>
      </section>
    </body>
  );
};

export default SignupPage;
