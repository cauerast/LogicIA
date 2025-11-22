import os
import json
from fastapi import APIRouter, HTTPException
from schemas import TranslationRequest
from google import genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=os.environ.get(GEMINI_API_KEY))


home_router = APIRouter(prefix="/translate", tags=["Translate"])

def call_ai_translator(text: str, propositions: dict, direction: str = "nl_to_cpc") -> dict:
   
    if direction == "nl_to_cpc":
        prompt = f"""
        Você é um tradutor de lógica proposicional.
        Traduza o texto abaixo de Linguagem Natural (NL) para Cálculo Proposicional Clássico (CPC).

        Texto NL: "{text}"

        Use as seguintes proposições (se fornecidas): {propositions if propositions else "{}"}.
        Caso não sejam fornecidas, gere automaticamente letras (A, B, C... ate T).

        Regras de mapeamento:
        "e" / "tambem" / "também" → ∧  
        "ou" → v  
        "não" / "nao" → ¬  
        "se...então" → →  
        "se e somente se" / "somente se" → ↔  

        Retorne APENAS um JSON válido neste formato exato: Caso o usuario nao informar nada nos campos ou informar qualquer coisa que seja diferente de um texto para tradução, retorne "". Voce é um programa que só traduz.
        {{
          "formula": "A ∧ B v ¬C",
          "propositions": {{
            "A": "texto da primeira proposição",
            "B": "texto da segunda proposição",
            "C": "texto da terceira proposição"
          }}
        }}
        """
    else:
        prompt = f"""
        Você é um tradutor de lógica proposicional.
        Traduza o texto abaixo de Cálculo Proposicional Clássico (CPC) para Linguagem Natural (NL).

        Texto CPC: "{text}"

        Use os seguintes significados de proposições (se fornecidos): {propositions if propositions else "{}"}.
        Caso não sejam fornecidos, gere significados genéricos como "Significado de A", etc.

        Regras de mapeamento inversas:
        ∧ → e  
        v → ou  
        ¬ → não  
        → → então  
        ↔ → se e somente se  

        Retorne APENAS um JSON válido neste formato exato: (caso o usuário, nao informe as proposições, crie proposições válidas com temas relacionados a animais fofinhos usando por exemplo Brownie (coelho), Lya (gatinha), Catarina (gatinha), Sheldon (gatinho)) caso precise de mais animais fofos, o crie. Caso o usuario nao informar nada nos campos ou informar qualquer coisa que seja diferente de um texto para tradução, retorne "". Voce é um programa que só traduz.
        {{
          "natural_language": "texto traduzido (retirar os parenteses da resposta)",
          "propositions": {{
            "A": "significado da proposição A",
            "B": "significado da proposição B"
          }}
        }}
        """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        raw_text = response.text.strip()

        # Tenta extrair apenas o JSON
        json_start = raw_text.find("{")
        json_end = raw_text.rfind("}") + 1
        json_str = raw_text[json_start:json_end]

        parsed = json.loads(json_str)
        return parsed

    except Exception as e:
        return {
            "error": f"Erro ao processar a resposta: {str(e)}",
            "raw_response": response.text if 'response' in locals() else None
        }



@home_router.get("/")
async def home():
    return {
        "message": "Welcome to LogicIA!",
        "description": "Translation of logical propositions CPC ↔ NL (A-T only).",
        "routes": {
            "nl_to_cpc": "/translate/nl_to_cpc",
            "cpc_to_nl": "/translate/cpc_to_nl"
        }
    }


@home_router.post("/nl_to_cpc")
async def nl_to_cpc(payload: TranslationRequest):
    if not payload.text or payload.text.strip() == "":
        raise HTTPException(status_code=400, detail="Texto vazio não pode ser traduzido.")

    translated = call_ai_translator(payload.text, payload.propositions, direction="nl_to_cpc")

    return {
        "original": payload.text,
        "translated": translated
    }


@home_router.post("/cpc_to_nl")
async def cpc_to_nl(payload: TranslationRequest):
    if not payload.text or payload.text.strip() == "":
        raise HTTPException(status_code=400, detail="Texto vazio não pode ser traduzido.")

    translated = call_ai_translator(payload.text, payload.propositions, direction="cpc_to_nl")

    return {
        "original": payload.text,
        "translated": translated
    }
