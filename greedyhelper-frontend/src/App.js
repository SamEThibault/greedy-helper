import { Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./pages/home/Home.js";
import Login from "./pages/login/Login.js";
import Signup from "./pages/signup/Signup.js";

function App() {
  return (
    <div>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </div>
  );
}

export default App;
