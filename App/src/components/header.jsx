// Imports
import React from "react";
import "./css/header.css";
import Logo from "../assets/logo-removebg-preview.png";

import { Link } from "react-router-dom";

function Header() {
  return (
    <header className="header">
      <Link to="/">
        <img src={Logo} alt="Logo" className="logo" />
      </Link>
    </header>
  );
}

export default Header;
