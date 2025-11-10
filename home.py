from typing import Any


from fastapi import APIRouter, HTTPException
from schemas import TranslationRequest
import re
import random

home_router = APIRouter(prefix="/translate", tags=["Translate"])


NL_TO_CPC = {
    r"\b e \b|\btambem\b|\btambém\b": " ∧ ",
    r"\b ou \b": " v ",
    r"\bnao\b|\bnão\b": "¬",
    r"\bse\b.*\bentao\b|\bentão\b": " → ",
    r"\bse e somente se\b|\bsomente se\b": " ↔ ",
}

CPC_TO_NL = {
    r"∧|\^": "e",
    r"V|v": "ou",
    r"¬|~": "não",
    r"→": "então",
    r"↔": "se e somente se"
}


VALID_LETTERS = list[str]("ABCDEFGHIJKLMNOPQRST")



def generate_random_propositions(sentences: list) -> dict:
    available_letters = VALID_LETTERS.copy()
    random.shuffle(available_letters)
    propositions = {}
    for i, sent in enumerate(sentences): # for i in range(len(sentences))
        if i < len(available_letters):
            propositions[available_letters[i]] = sent.strip() # sentences[i].strip()
    return propositions


def extract_propositions(text: str) -> list:

    # Remove pontuação desnecessária
    clean_text = re.sub(r"[.,!?]", "", text.lower())

    # Divide o texto por conectivos conhecidos
    parts = re.split(r"\b e \b|\btambem\b|\btambém\b|\b ou \b|\bnao\b|\bnão\b|\bse\b.*\bentao\b|\bentão\b|\bse e somente se\b|\bsomente se\b", clean_text)

    # Limpa espaços e remove strings vazias
    return [p.strip() for p in parts if p.strip()]



def translate_nl_to_cpc(text: str, user_props: dict = None) -> dict:
    processed = text.lower()

    # Substitui conectivos por símbolos CPC
    for pattern, replacement in NL_TO_CPC.items():
        processed = re.sub(pattern, replacement, processed)

    # Extrai proposições simples automaticamente
    sentences = extract_propositions(text)

    # Usa as proposições fornecidas ou gera automaticamente
    if user_props and len(user_props) > 0:
        propositions = user_props
    else:
        random_props = generate_random_propositions(sentences)

        repeated_props_remover = set()
        propositions = {}
        for prop, meaning in random_props.items():
            normalized = meaning.lower().strip()
            if normalized not in repeated_props_remover:
                propositions[prop] = meaning
                repeated_props_remover.add(normalized)

    # Substitui proposições por letras (A–T)
    formula = processed
    for prop, meaning in propositions.items():
        # Evita substituir dentro de palavras
        formula = re.sub(re.escape(meaning.lower()), prop, formula)

    return {
        "formula": formula.strip(),
        "propositions": propositions
    }



def translate_cpc_to_nl(text: str, user_props: dict = None) -> dict:
    # Detecta proposições existentes (A–T)
    props_found = sorted(set[Any](re.findall(r"\b[A-T]\b", text)))

    # Se o usuário não informou, cria significados padrão
    if not user_props:
        user_props = {p: f"Significado de {p}" for p in props_found}

    # Substitui proposições pelos significados
    result_text = text
    for prop, meaning in user_props.items():
        result_text = re.sub(rf"\b{prop}\b", meaning, result_text)

    # Substitui operadores lógicos
    for pattern, meaning in CPC_TO_NL.items():
        result_text = re.sub(pattern, f"{meaning}", result_text)

    return {
        "natural_language": result_text.strip(),
        "propositions": user_props
    }


# ==== Routes ====
@home_router.get("/")
async def home():
    return {
        "message": "Welcome to LogicIA!",
        "description": "Translation of logical propositions CPC ↔ NL (A–T only).",
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
