import { useState } from "react";
import Box from "../components/box";
import "./css/style.css";
import Teles from "../assets/teles-removebg-preview.png"; 
import { useNavigate } from "react-router-dom";

function NL() {
  const [showContent, setShowContent] = useState(false);
  const navigate = useNavigate();

  const handleClick = () => {
    setShowContent(true);
  };

  const handleNavigate = () => {
    navigate("/introduction");
  };

  const reiniciar = () => {
    window.location.reload();
  }

  return (
    <section>
      <Box style={{ height: "425px" }}>
        <p className="modo">MODO</p>

        <div className="containerModo">NL → CPC</div>

        <p className="nlText">
          ESCREVA A SENTENÇA EM LINGUAGEM NATURAL:
        </p>

        <input
          type="text"
          className="nlInput"
          placeholder="Digite aqui..."
        />

        <div className="containerButtonNL">
          <button className="nlButton" onClick={handleClick}>
            MOSTRAR RESULTADO
          </button>

          <button className="nlButton" onClick={handleNavigate}>
            ALTERAR MODO
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
                <p>A fórmula em CPC é: ............................................................</p>
              </div>
            </div>
          </div>

          {/* BOTÃO CENTRALIZADO EMBAIXO DE TUDO */}
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
