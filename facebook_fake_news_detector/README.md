# Facebook Fake News Detector

A starter full-stack project for detecting potentially misleading Facebook posts.

## Stack
- Frontend: React + Vite
- Backend: FastAPI
- ML: scikit-learn TF-IDF + Logistic Regression
- CORS enabled for local development

## Project structure

```text
facebook_fake_news_detector/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── model.py
│   │   └── schemas.py
│   ├── data/
│   │   └── sample_news.csv
│   ├── requirements.txt
│   └── train_model.py
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   └── index.html
└── README.md
```

## Run the backend

```bash
cd backend
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Train the starter model:
```bash
python train_model.py
```

Start FastAPI:
```bash
uvicorn app.main:app --reload
```

Backend runs at:
http://127.0.0.1:8000

API documentation:
http://127.0.0.1:8000/docs

## Run the frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Then open the Vite URL shown in the terminal.

## Important

The included dataset is intentionally tiny and is only for demonstrating the pipeline. It is NOT suitable for claiming high real-world accuracy.

For a serious project, replace it with a properly labeled dataset and later add:
- Nepali/Romanized Nepali support
- claim extraction
- URL/source analysis
- evidence retrieval
- reliable-source verification
- image/meme analysis
- explainable confidence
- database/history
- Facebook integration only where permitted by Meta's APIs and policies
