import { useState } from "react";
import Box from "../components/box";
import "./css/style.css";
import Teles from "../assets/teles-removebg-preview.png";
import { useNavigate } from "react-router-dom";

function NL() {
  const [showContent, setShowContent] = useState(false);
  const [formula, setFormula] = useState("");
  const [propositions, setPropositions] = useState("");
  const navigate = useNavigate();

  const handleClick = async () => {
    try {
      const frase = document.getElementById("frase").value;
  
      const data = await fetch("http://127.0.0.1:8000/translate/nl_to_cpc", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: frase,
          propositions: {},
        }),
      });
  
      const response = await data.json();
  
      setFormula(response.translated.formula);

      const propsObject = response.translated.propositions;
      const formattedProps = Object.entries(propsObject)
        .map(([key, value]) => `\t${key}: ${value}`)
        .join("\n");
  
      setPropositions(formattedProps);
  
      setShowContent(true);
    } catch (erro) {
      console.log(erro);
    }
  };

  const handleNavigate = () => {
    navigate("/introduction");
  };

  const reiniciar = () => {
    window.location.reload();
  };

  return (
    <section>
      <Box style={{ height: "400px" }}>
        <p className="modo">MODO</p>

        <button className="containerModo" onClick={handleNavigate}>NL → CPC</button>

        <p className="nlText">ESCREVA A SENTENÇA EM LINGUAGEM NATURAL:</p>

        <input
          type="text"
          className="nlInput"
          placeholder="Digite aqui..."
          id="frase"
        />

        <div className="containerButtonNL">
          <button className="nlButton" onClick={handleClick}>
            MOSTRAR RESULTADO
          </button>
        </div>
      </Box>

      {showContent && (
        <>
          <div className="containerRespostaNL">
            <img src={Teles} alt="Teles" className="telesResposta" />

            <div className="solucaoContainer">
              <h2 className="solucaoTitle">SOLUÇÃO</h2>
              <div className="solucaoBox">
              Formula: {formula}
              <br />
              Propositions:
              <pre className="propsBox">{propositions}</pre>

              </div>
            </div>
          </div>

          <div className="containerReiniciar">
            <button className="btnReiniciar" onClick={reiniciar}>
              REINICIAR
            </button>
          </div>
        </>
      )}
    </section>
  );
}

export default NL;
