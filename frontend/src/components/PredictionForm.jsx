
import { useState } from "react";
import API from "../services/api";
import ResultCard from "./ResultCard";

function PredictionForm() {

  const [text, setText] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  // =====================================
  // PREDICT
  // =====================================
  const predictNews = async () => {

    setError("");

    // VALIDATION
    if (!text.trim()) {
      setError("Please enter Tigrigna news text.");
      return;
    }

    try {

      setLoading(true);

      const response = await API.post("/predict", {
        text: text.trim(),
      });

      setResult(response.data);

    } catch (error) {

      console.log(error);

      // SHOW BACKEND ERROR
      if (error.response?.data?.detail) {
        setError(error.response.data.detail);
      } else {
        setError("Backend connection failed.");
      }
    }

    finally {
      setLoading(false);
    }
  };

  // =====================================
  // CLEAR
  // =====================================
  const clearAll = () => {

    setText("");

    setResult(null);

    setError("");
  };

  return (

    <div
      id="predict-section"
      className="bg-[#111827] p-6 rounded-2xl shadow-lg border border-gray-700"
    >

      {/* LABEL */}
      <h2 className="text-2xl font-bold mb-5 text-white">

        Enter Tigrigna News Text

      </h2>

      {/* TEXTAREA */}
      <textarea
        rows="10"
        placeholder="Paste Tigrigna news text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="w-full bg-[#1f2937] text-white p-4 rounded-xl outline-none border border-gray-600 focus:border-cyan-400 transition resize-none"
      />

      {/* ERROR */}
      {error && (
        <p className="text-red-400 mt-4">
          {error}
        </p>
      )}

      {/* BUTTONS */}
      <div className="flex justify-between mt-5">

        <button
          onClick={clearAll}
          className="bg-red-500 hover:bg-red-600 px-6 py-3 rounded-xl font-semibold transition"
        >
          Clear
        </button>

        <button
          onClick={predictNews}
          disabled={loading}
          className="bg-cyan-400 text-black hover:bg-cyan-500 px-6 py-3 rounded-xl font-semibold transition"
        >
          {loading ? "Analyzing..." : "Predict"}
        </button>

      </div>

      {/* RESULT */}
      <div className="mt-6">

        <ResultCard result={result} />

      </div>

    </div>
  );
}

export default PredictionForm;

