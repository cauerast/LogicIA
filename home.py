from fastapi import APIRouter, HTTPException
from schemas import TranslationRequest
import re

# home router
home_router = APIRouter(prefix="/translate", tags=["Translate"])

# Translate Dicts
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

# home endpoint
@home_router.get("/")
async def home():
    return {
        "message": "Welcome to LogicIA! ",
        "description": "Translation of logical propositions CPC ↔ NL.",
        "routes": {
            "nl_to_cpc": "/translate/nl_to_cpc",
            "cpc_to_nl": "/translate/cpc_to_nl"
        }
    }


@home_router.post("/cpc_to_nl")
async def cpc_to_nl(payload: TranslationRequest):
    
    pass

    return {
        "original": "{payload.text}", 
        "translated": "{translated}"
        }


@home_router.post("/nl_to_cpc")
async def nl_to_cpc(payload: TranslationRequest):

    pass

    return {
        "original": "{payload.text}",
        "translated": "{translated}"
    }