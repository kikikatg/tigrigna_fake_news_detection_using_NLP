import { useState } from "react";
import axios from "axios";

export default function Feedback({ result, newsText }) {
  const [sent, setSent] = useState(false);
  const [loading, setLoading] = useState(false);

  if (!result) return null;

  const handleFeedback = async (correctLabel) => {
    if (loading || sent) return;

    setLoading(true);

    try {
      await axios.post("http://127.0.0.1:8000/feedback", {
        text: newsText,
        predicted: result.label,
        correct: correctLabel,
      });

      setSent(true);

    } catch (error) {
      console.error("Feedback error:", error);
      alert("Failed to send feedback. Check backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="text-center mt-6">

      <p className="mb-4 text-gray-300">
        Was the prediction correct?
      </p>

      {sent ? (
        <p className="text-green-400 font-semibold">
          ✅ Thank you for your feedback!
        </p>
      ) : (
        <div className="flex justify-center gap-4">

          <button
            disabled={loading}
            onClick={() => handleFeedback("REAL")}
            className="bg-green-500 hover:bg-green-600 px-6 py-2 rounded-full disabled:opacity-50"
          >
            👍 Real
          </button>

          <button
            disabled={loading}
            onClick={() => handleFeedback("FAKE")}
            className="bg-red-500 hover:bg-red-600 px-6 py-2 rounded-full disabled:opacity-50"
          >
            👎 Fake
          </button>

        </div>
      )}
    </div>
  );
}