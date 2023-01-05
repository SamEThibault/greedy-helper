import React from "react";
import "./Signup.css";
import { Link } from "react-router-dom";
function Signup() {
  return (
    <>
      <div>Signup</div>

      <Link to="/home" className="navbar-logo">
        <h1>Home</h1>
      </Link>
    </>
  );
}

export default Signup;
