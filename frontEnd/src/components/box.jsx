// src/components/box.jsx
import React from "react";
import "./css/box.css";

function Box({ children, style }) {
  return (
    <div className="container">
      <div className="box" style={style}>
        {children}
      </div>
    </div>
  );
}

export default Box;
