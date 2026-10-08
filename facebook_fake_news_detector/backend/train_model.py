from pathlib import Path
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "sample_news.csv"
OUTPUT = BASE / "model.joblib"

df = pd.read_csv(DATA)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        max_features=5000
    )),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(df["text"], df["label"])
joblib.dump(model, OUTPUT)

print(f"Model trained on {len(df)} sample records.")
print(f"Saved to: {OUTPUT}")
