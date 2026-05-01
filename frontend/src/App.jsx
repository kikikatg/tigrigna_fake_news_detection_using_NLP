import { useState } from "react";
import Header from "./components/Header";
import InputBox from "./components/InputBox";
import ResultCard from "./components/ResultCard";
import Feedback from "./components/Feedback";

function App() {
  const [newsText, setNewsText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="min-h-screen bg-[#0f172a] text-white flex flex-col items-center p-6">
      <Header />

      <div className="w-full max-w-3xl mt-10">
        <InputBox
          newsText={newsText}
          setNewsText={setNewsText}
          setResult={setResult}
          setLoading={setLoading}
        />

        <div className="mt-8">
          <ResultCard result={result} loading={loading} />
        </div>

        <div className="mt-8">
          <Feedback result={result} newsText={newsText} />
        </div>
      </div>
    </div>
  );
}

export default App;