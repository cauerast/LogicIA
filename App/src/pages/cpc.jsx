import { useState } from "react";
import Box from "../components/box";
import "./css/style.css";
import Teles from "../assets/teles-removebg-preview.png";
import { useNavigate } from "react-router-dom";

function CPC() {
  const [showContent, setShowContent] = useState(false);
  const [natural_language, setNatural_language] = useState("");
  const [propositions, setPropositions] = useState("");
  const navigate = useNavigate();

  const handleClick = async () => {
    try {
      const frase = document.getElementById("frase").value;
      const propositions = document.getElementById("propositions").value;
  
      const data = await fetch("https://logicia.onrender.com/translate/cpc_to_nl", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: frase,
          propositions: {propositions},
        }),
      });
  
      const response = await data.json();
  
      setNatural_language(response.translated.natural_language);

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
      <Box style={{ height: "550px" }}>
        <p className="modo">MODO</p>

        <button className="containerModo" onClick={handleNavigate}>CPC → NL</button>
        

        <p className="cpcText">ESCREVA A SENTENÇA EM LINGUAGEM CPC: </p>

        <input
          type="text"
          className="cpcInput"
          placeholder="Digite aqui..."
          id="frase"
        />

        <p className="cpcText">INFORME O SIGNIFICADO DAS PROPOSIÇÕES: </p>
        <input
          type="text"
          className="cpcInput"
          placeholder="(Opcional)"
          id="propositions"
        />

        <div className="containerButtonCPC">
          <button className="cpcButton" onClick={handleClick}>
            MOSTRAR RESULTADO
          </button>
        </div>
      </Box>

      {showContent && (
        <>
          <div className="containerRespostaCPC">
            <img src={Teles} alt="Teles" className="telesResposta" />

            <div className="solucaoContainer">
              <h2 className="solucaoTitle">SOLUÇÃO</h2>
              <div className="solucaoBox">
              Frase: {natural_language}
              <br />
              Poposições:
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

export default CPC;
