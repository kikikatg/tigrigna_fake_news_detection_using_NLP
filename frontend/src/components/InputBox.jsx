import { predictNews } from "../services/api";

export default function InputBox({
  newsText,
  setNewsText,
  setResult,
  setLoading,
}) {
  const handlePredict = async () => {
    if (!newsText.trim()) {
      alert("Please enter some news text");
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const data = await predictNews(newsText);

      setResult({
        label: data.label,
        confidence: data.confidence,
        risk_level: data.risk_level,
      });

    } catch (error) {
      console.error(error);
      alert("Backend error. Check FastAPI.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="text-center">
      <h2 className="text-3xl font-bold mb-6">
        Check if news is real or fake!
      </h2>

      <textarea
        value={newsText}
        onChange={(e) => setNewsText(e.target.value)}
        placeholder="Enter the news here..."
        className="w-full h-40 p-4 rounded-xl text-black outline-none"
      />

      <button
        onClick={handlePredict}
        className="mt-5 bg-blue-500 hover:bg-blue-600 px-6 py-2 rounded-full font-bold"
      >
        Predict
      </button>
    </div>
  );
}