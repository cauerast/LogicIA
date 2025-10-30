from fastapi import APIRouter, HTTPException
from schemas import TranslationRequest
import re

home_router = APIRouter(prefix="/translate", tags=["Translate"])

NL_TO_CPC = {
    r"\b e \b": " ∧ ",
    r"\b ou \b": " v ",
    r"\b nao\b|\b não\b": " ¬ ",
    r"\bse\b.*\bentao\b|\bentão\b": " → ",
    r"\bse e somente se\b|\bsomente se\b": " ↔ ",
}

CPC_TO_NL = {
    "∧": "e",
    "v": "ou",
    "¬": "não",
    "→": "então",
    "↔": "se e somente se"
}

# translate functions
def translate_nl_to_cpc(text: str, user_props: dict = None) -> dict:
   
    processed = text.lower()

    # Aplica substituições dos conectivos
    for pattern, replacement in NL_TO_CPC.items():
        processed = re.sub(pattern, replacement, processed)
        

    # Divide frases em proposições simples
    sentences = re.split(r"[.!?]", text)
    propositions = {}
    if user_props:
        propositions = user_props
    else:
        # Gera proposições automáticas (A, B, C...)
        for i, sent in enumerate(sentences):
            if sent.strip():
                propositions[chr(65 + i)] = sent.strip()  # A, B, C...

    # Substitui frases pelas proposições
    formula = processed
    for prop, meaning in propositions.items():
        formula = formula.replace(meaning.lower(), prop)

    return {
        "formula": formula,
        "propositions": propositions
    }

def translate_cpc_to_nl(text: str, user_props: dict = None) -> dict:
    
    if user_props is None:
        # Detecta proposições automaticamente (A, B, C...)
        props_found = sorted(set(re.findall(r"\b[A-Z]\b", text)))
        user_props = {p: f"Significado de {p}" for p in props_found}

    # Substitui proposições pelo significado informado
    result_text = text
    for prop, meaning in user_props.items():
        result_text = re.sub(rf"\b{prop}\b", meaning, result_text)

    # Substitui operadores lógicos
    for symbol, meaning in CPC_TO_NL.items():
        result_text = result_text.replace(symbol, f" {meaning} ")

    return {
        "natural_language": result_text.strip(),
        "propositions": user_props
    }

# ==== ROTAS ====
@home_router.get("/")
async def home():
    return {
        "message": "Welcome to LogicIA!",
        "description": "Translation of logical propositions CPC ↔ NL.",
        "routes": {
            "nl_to_cpc": "/translate/nl_to_cpc",
            "cpc_to_nl": "/translate/cpc_to_nl"
        }
    }

@home_router.post("/nl_to_cpc")
async def nl_to_cpc(payload: TranslationRequest):
    if not payload.text or payload.text.strip() == "":
        raise HTTPException(status_code=400, detail="Texto vazio não pode ser traduzido.")
    
    translated = translate_nl_to_cpc(payload.text, payload.propositions)

    return {
        "original": payload.text,
        "translated": translated
    }

@home_router.post("/cpc_to_nl")
async def cpc_to_nl(payload: TranslationRequest):
    if not payload.text or payload.text.strip() == "":
        raise HTTPException(status_code=400, detail="Texto vazio não pode ser traduzido.")

    translated = translate_cpc_to_nl(payload.text, payload.propositions)

    return {
        "original": payload.text,
        "translated": translated
    }
