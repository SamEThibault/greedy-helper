import React from "react";
import "./Home.css";
import { Link } from "react-router-dom";

function Home() {
  return (
    <>
      <div>hello</div>

      <Link to="/login" className="navbar-logo">
        <h1>Log in</h1>
      </Link>
    </>
  );
}

export default Home;
