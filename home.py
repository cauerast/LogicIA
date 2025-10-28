from fastapi import APIRouter, HTTPException
from schemas import TranslationRequest

# home router
home_router = APIRouter(prefix="/translate", tags=["Translate"])

# home endpoint
@home_router.get("/")
async def home():
    return {
        "message": "Welcome to LogicIA! ",
        "description": "Translation of logical propositions CPC ↔ NL.",
        "routes": {
            "nl_to_cpc": "/home/nl-to-cpc",
            "cpc_to_nl": "/home/cpc-to-nl"
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