//Imports
import Box from "../components/box";
import "./css/style.css";

import Pilastra1 from "../assets/pilastra2.png";
import Pilastra2 from "../assets/pilastra1.png";
import Teles from "../assets/teles-removebg-preview.png";

import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  function handleNavigate() {
    navigate("/introduction");
  }

  const handleClick = async () => {
    try {
      const data = (await fetch("https://logicia.onrender.com/translate/")).json()
      console.log(data)

    } catch (erro) {
      console.log(erro);
    }
  };

  return (
    <section>
      <Box>
        <img src={Pilastra1} alt="Pilastra" className="pilastra1" />
        <img src={Pilastra2} alt="Pilastra" className="pilastra2" />
        <img src={Teles} alt="Teles" className="teles" />

        <div className="container">
          <div className="containerTexts">
            <p className="title">Bem vindo à LogicIA!</p>
            <p className="textWelcome">
              LogicIA é uma inteligência artificial criada para conectar a
              linguagem natural com a linguagem da lógica proposicional. 
              Com ela, você pode transformar frases comuns em expressões 
              do CPC e traduzir fórmulas lógicas de volta para a linguagem natural, 
              de forma rápida e clara!.
            </p>
          </div>
        </div>

        <div className="containerButton">
          <button className="btnIniciar" onClick={() => {
            handleClick();
            handleNavigate();
          }}>
            Vamos lá!
          </button>
        </div>
      </Box>
    </section>
  );
}

export default Home;
