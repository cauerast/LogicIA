from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    propositions: dict

    class Config:
        from_attributes = True