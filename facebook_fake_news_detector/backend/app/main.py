from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import NewsRequest, NewsResponse
from .model import get_model

app = FastAPI(
    title="Facebook Fake News Detector API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def red_flags(text: str) -> list[str]:
    flags = []
    lower = text.lower()

    if "share this" in lower or "share now" in lower:
        flags.append("Uses urgent sharing language.")
    if "breaking" in lower or "urgent" in lower:
        flags.append("Uses sensational/urgent wording.")
    if "facebook deletes" in lower or "before facebook" in lower:
        flags.append("Uses a 'share before it is deleted' style claim.")
    if "everyone will receive" in lower or "free money" in lower:
        flags.append("Promises an unusually broad reward.")
    if "secret" in lower or "doctors are hiding" in lower:
        flags.append("Uses secrecy/conspiracy-style wording.")
    if "!!!" in text:
        flags.append("Uses excessive punctuation.")

    return flags

@app.get("/")
def root():
    return {"message": "Facebook Fake News Detector API is running"}

@app.post("/predict", response_model=NewsResponse)
def predict(request: NewsRequest):
    try:
        model = get_model()
        prediction = model.predict([request.text])[0]
        probabilities = model.predict_proba([request.text])[0]
        classes = list(model.classes_)
        confidence = float(probabilities[classes.index(prediction)]) * 100

        verdict = "LIKELY FAKE" if prediction == "fake" else "LIKELY REAL"

        reasons = red_flags(request.text)
        if not reasons:
            reasons.append(
                "The starter ML model found no obvious rule-based red flags."
            )

        return NewsResponse(
            verdict=verdict,
            confidence=round(confidence, 2),
            reasons=reasons
        )
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
