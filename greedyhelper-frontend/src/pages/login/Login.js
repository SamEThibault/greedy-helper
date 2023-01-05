import React from "react";
import "./Login.css";
import { Link } from "react-router-dom";
function Login() {
  return (
    <>
      <div>Login</div>
      
      <Link to="/signup" className="navbar-logo">
        <h1>Sign up</h1>
      </Link>

      <Link to="/" className="navbar-logo">
        <h1>Home</h1>
      </Link>
    </>
  );
}

export default Login;
