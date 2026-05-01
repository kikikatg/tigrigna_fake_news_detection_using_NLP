export default function Feedback({ result, newsText }) {
  if (!result) return null;

  const handleFeedback = (correctLabel) => {
    console.log("User Feedback:", {
      text: newsText,
      predicted: result.label,
      correct: correctLabel,
    });

    // later → send to backend
  };

  return (
    <div className="text-center">
      <p className="mb-4">
        Give us some feedback if we predicted it wrong :)
      </p>

      <div className="flex justify-center gap-4">
        <button
          onClick={() => handleFeedback("REAL")}
          className="bg-green-500 hover:bg-green-600 px-6 py-2 rounded-full"
        >
          Real
        </button>

        <button
          onClick={() => handleFeedback("FAKE")}
          className="bg-red-500 hover:bg-red-600 px-6 py-2 rounded-full"
        >
          Fake
        </button>
      </div>
    </div>
  );
}