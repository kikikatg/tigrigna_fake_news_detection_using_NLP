
export default function ResultCard({ result, loading }) {
  if (loading) {
    return (
      <div className="text-center">
        <p className="text-lg animate-pulse">Analyzing...</p>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="text-center text-gray-400">
        <p>No prediction yet</p>
      </div>
    );
  }

  const { label, confidence, risk_level } = result;

  const isReal = label === "REAL";

  return (
    <div className="text-center bg-gray-900 p-6 rounded-xl mt-6">
      <h2
        className={`text-3xl font-bold ${
          isReal ? "text-green-400" : "text-red-400"
        }`}
      >
        {label}
      </h2>

      <p className="mt-2 text-sm text-gray-300">
        Risk Level: {risk_level}
      </p>

      <div className="w-full bg-gray-700 rounded-full h-4 mt-4 overflow-hidden">
        <div
          className={`h-4 rounded-full ${
            isReal ? "bg-green-500" : "bg-red-500"
          }`}
          style={{ width: `${confidence}%` }}
        />
      </div>

      <p className="mt-3">
        Confidence: {confidence.toFixed(2)}%
      </p>
    </div>
  );
}

