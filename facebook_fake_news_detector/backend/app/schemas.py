from pydantic import BaseModel, Field

class NewsRequest(BaseModel):
    text: str = Field(..., min_length=5)

class NewsResponse(BaseModel):
    verdict: str
    confidence: float
    reasons: list[str]
