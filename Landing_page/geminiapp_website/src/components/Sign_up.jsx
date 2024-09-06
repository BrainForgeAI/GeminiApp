import React, { useState } from "react";
import "../styles/signup.css";

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
              <label className="form-label" htmlFor="fname">
                Name
              </label>
              <input
                className="form-input"
                type="text"
                id="fname"
                name="name"
                placeholder="John Doe"
                value={formData.name}
                onChange={handleChange}
              />
            </div>
            <div className="form-subbox">
              <label className="form-label" htmlFor="femail">
                Email
              </label>
              <input
                className="form-input"
                type="email"
                id="femail"
                name="email"
                placeholder="JohnDoe@email.com"
                value={formData.email}
                onChange={handleChange}
              />
            </div>
            <div className="form-subbox">
              <label className="form-label" htmlFor="fpassword">
                Password
              </label>
              <input
                className="form-input"
                type="password"
                id="fpassword"
                name="password"
                placeholder="Enter your password"
                value={formData.password}
                onChange={handleChange}
              />
            </div>
            <div className="form-subbox">
              <button type="submit">Sign Up</button>
            </div>
          </form>
        </div>
      </section>
    </body>
  );
};

export default SignupPage;
