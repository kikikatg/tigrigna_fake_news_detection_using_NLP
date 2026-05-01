import { useState } from "react";

export default function Header() {
  const [dark, setDark] = useState(true);

  return (
    <div className="w-full flex justify-between items-center">
      <h1 className="text-xl font-bold">Fake News Prediction</h1>

      <div className="flex items-center gap-3">
        <span>Dark Mode</span>
        <button
          onClick={() => setDark(!dark)}
          className="w-12 h-6 bg-red-500 rounded-full relative"
        >
          <div className={`w-5 h-5 bg-white rounded-full absolute top-0.5 transition-all ${dark ? "right-0.5" : "left-0.5"}`} />
        </button>
      </div>
    </div>
  );
}