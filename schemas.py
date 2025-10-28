from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str

    class Config:
        from_attributes = True