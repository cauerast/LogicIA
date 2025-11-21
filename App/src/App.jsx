// App.jsx
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// pages
import Home from "./pages/home";
import Introduction from "./pages/introduction";
import NL from "./pages/nl";
import CPC from "./pages/cpc";

//components
import Header from "./components/header";

function App() {
  return (
    <Router>
      <Header /> 
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/introduction" element={<Introduction />} />
        <Route path="/nl" element={<NL />} />
        <Route path="/cpc" element={<CPC />} />
      </Routes>
      
    </Router>
  );
}

export default App;
