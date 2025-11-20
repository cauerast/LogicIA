import Box from "../components/box";
import "./css/style.css";

import Teles from "../assets/teles-removebg-preview.png";

import { useNavigate } from "react-router-dom";

function Introduction() {

  const navigate = useNavigate();
  function NlNavigate() {
    navigate("/nl")
  }
  function CpcNavigate(){
    navigate("/cpc")
  }

  return (
    <section>
      <Box>
        <div className="boxInt">
          <img src={Teles} alt="Teles" className="telesInt" />
          <div className="containerInt">
            <p className="saudacao">
              Olá! Eu sou o Teles, o mascote da LogicIA! 🧠
            </p>
            <p className="paragrafo">
              Vim para te ajudar nas traduções do CPC (Cálculo Proposicional
              Clássico) — transformando frases da linguagem natural em lógica
              formal e vice-versa, de um jeito simples e intuitivo. <strong> Então, por
              onde começamos?</strong>
            </p>
          </div>
        </div>
        <div className="containerButtonInt">
                <button className="btnInt" onClick={NlNavigate}>
                    NL   →   CPC
                </button>
                <button className="btnInt" onClick={CpcNavigate}>
                    CPC   →   NL
                </button>
        </div>
      </Box>
    </section>
  );
}

export default Introduction;
