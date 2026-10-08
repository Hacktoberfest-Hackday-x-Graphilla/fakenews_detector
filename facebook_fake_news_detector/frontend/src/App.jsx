import { useState } from "react";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function analyzePost() {
    if (!text.trim()) return;

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong");
      }

      setResult(data);
    } catch (err) {
      setError(
        `${err.message}. Make sure the FastAPI backend is running.`
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="container">
      <section className="hero">
        <p className="eyebrow">AI / ML PROJECT</p>
        <h1>Facebook Fake News Detector</h1>
        <p className="subtitle">
          Paste a Facebook post and analyze whether it is likely to be fake
          or real.
        </p>
      </section>

      <section className="card">
        <label htmlFor="post">Facebook post</label>
        <textarea
          id="post"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Paste the Facebook post here..."
          rows="9"
        />

        <button onClick={analyzePost} disabled={loading || !text.trim()}>
          {loading ? "Analyzing..." : "Analyze Post"}
        </button>

        {error && <div className="error">{error}</div>}
      </section>

      {result && (
        <section className="result card">
          <p className="eyebrow">RESULT</p>
          <h2>{result.verdict}</h2>
          <div className="confidence">
            Confidence: <strong>{result.confidence}%</strong>
          </div>

          <h3>Why?</h3>
          <ul>
            {result.reasons.map((reason, index) => (
              <li key={index}>{reason}</li>
            ))}
          </ul>

          <p className="disclaimer">
            This is a starter ML system, not a definitive fact-checker.
            A production system should verify claims against reliable
            evidence before calling something false.
          </p>
        </section>
      )}

      <footer>
        Built with React + FastAPI + scikit-learn
      </footer>
    </main>
  );
}

export default App;
