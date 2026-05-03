function ResultCard({ result }) {

  if (!result) return null;

  const isReal = result.label === "REAL";

  return (

    <div className="bg-[#1f2937] border border-gray-700 rounded-3xl p-8 shadow-2xl">

      {/* HEADER */}
      <h2 className="text-3xl font-bold text-white mb-8">
        Prediction Result
      </h2>

      {/* RESULT */}
      <div className="flex flex-col items-center justify-center">

        <div
          className={`text-5xl font-extrabold mb-6 ${
            isReal
              ? "text-green-400"
              : "text-red-400"
          }`}
        >

          {isReal ? "🟢 REAL NEWS" : "🔴 FAKE NEWS"}

        </div>

        {/* CONFIDENCE TEXT */}
        <p className="text-xl text-gray-300 mb-4">

          Confidence:{" "}

          <span className="font-bold text-white">
            {result.confidence}%
          </span>

        </p>

        {/* PROGRESS BAR */}
        <div className="w-full max-w-xl h-5 bg-gray-700 rounded-full overflow-hidden">

          <div
            className={`h-full transition-all duration-700 ${
              isReal
                ? "bg-green-400"
                : "bg-red-400"
            }`}
            style={{
              width: `${result.confidence}%`,
            }}
          />

        </div>

      </div>

    </div>
  );
}

export default ResultCard;