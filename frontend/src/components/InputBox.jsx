import { useState } from "react";

function InputBox({
  newsText,
  setNewsText,
  setResult,
  setLoading,
}) {
  const [error, setError] = useState("");

  const handlePredict = async () => {
    setError("");

    // VALIDATION
    if (!newsText.trim()) {
      setError("Please enter news text.");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            text: newsText,
          }),
        }
      );

      // HANDLE BACKEND ERROR
      if (!response.ok) {
        const err = await response.json();

        throw new Error(
          err.detail || "Prediction failed"
        );
      }

      const data = await response.json();

      setResult(data);

    } catch (err) {
      console.error(err);

      alert("Backend error. Check FastAPI.");

    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setNewsText("");
    setResult(null);
    setError("");
  };

  return (
    <div className="bg-[#111827] p-6 rounded-2xl border border-gray-700 shadow-xl">

      <h2 className="text-2xl font-bold mb-4">
        Analyze Tigrigna News
      </h2>

      <textarea
        value={newsText}
        onChange={(e) => setNewsText(e.target.value)}
        placeholder="Paste Tigrigna news article here..."
        className="w-full h-56 bg-[#0f172a] border border-gray-700 rounded-xl p-4 text-white outline-none focus:border-cyan-400 resize-none"
      />

      {error && (
        <p className="text-red-400 mt-3">
          {error}
        </p>
      )}

      <div className="flex justify-between mt-5">

        <button
          onClick={handleClear}
          className="bg-red-500 hover:bg-red-600 px-6 py-3 rounded-xl font-semibold transition"
        >
          Clear
        </button>

        <button
          onClick={handlePredict}
          className="bg-cyan-400 hover:bg-cyan-500 text-black px-6 py-3 rounded-xl font-bold transition"
        >
          Predict
        </button>

      </div>
    </div>
  );
}

export default InputBox;