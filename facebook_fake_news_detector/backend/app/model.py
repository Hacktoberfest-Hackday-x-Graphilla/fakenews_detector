from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).resolve().parent.parent / "model.joblib"

_model = None

def get_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                "Model not found. Run: python train_model.py"
            )
        _model = joblib.load(MODEL_PATH)
    return _model
