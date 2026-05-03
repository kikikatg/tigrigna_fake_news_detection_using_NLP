import { useEffect, useState } from "react";
import API from "../services/api";

export default function History() {

  const [history, setHistory] = useState([]);

  const [loading, setLoading] = useState(true);

  const [showPopup, setShowPopup] = useState(false);

  // =====================================
  // FETCH HISTORY
  // =====================================
  const fetchHistory = async () => {

    try {

      const response = await API.get("/history");

      setHistory(response.data);

    } catch (error) {

      console.log(error);
    }

    finally {

      setLoading(false);
    }
  };

  // =====================================
  // CLEAR HISTORY
  // =====================================
  const clearHistory = async () => {

    try {

      await API.delete("/history");

      setHistory([]);

      // SHOW UI POPUP
      setShowPopup(true);

      setTimeout(() => {
        setShowPopup(false);
      }, 2500);

    } catch (error) {

      console.log(error);
    }
  };

  useEffect(() => {

    fetchHistory();

  }, []);

  return (

    <div className="max-w-6xl mx-auto px-6 py-10">

      {/* POPUP */}
      {showPopup && (
        <div className="fixed top-6 right-6 bg-red-500 text-white px-6 py-4 rounded-xl shadow-2xl z-50 animate-bounce">
          History cleared successfully
        </div>
      )}

      {/* HEADER */}
      <div className="flex justify-between items-center flex-wrap gap-4">

        <div>

          <h1 className="text-4xl font-extrabold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">

            Prediction History

          </h1>

          <p className="text-gray-400 mt-3 text-lg">

            Previously analyzed Tigrigna news articles.

          </p>

        </div>

        {/* CLEAR BUTTON */}
        {history.length > 0 && (
          <button
            onClick={clearHistory}
            className="bg-red-500 hover:bg-red-600 px-6 py-3 rounded-xl font-semibold transition"
          >
            Clear History
          </button>
        )}

      </div>

      {/* LOADING */}
      {loading ? (

        <div className="mt-10 text-gray-400">
          Loading history...
        </div>

      ) : history.length === 0 ? (

        <div className="mt-10 bg-[#111827] border border-gray-700 rounded-2xl p-8 text-center text-gray-400">

          No prediction history yet.

        </div>

      ) : (

        <div className="mt-10 grid gap-6">

          {history.map((item) => (

            <div
              key={item.id}
              className="bg-[#111827] border border-gray-700 rounded-2xl p-6 shadow-lg"
            >

              {/* TOP */}
              <div className="flex justify-between items-center flex-wrap gap-4">

                <div>

                  <span
                    className={`px-4 py-2 rounded-full text-sm font-bold ${
                      item.label === "REAL"
                        ? "bg-green-500/20 text-green-400"
                        : "bg-red-500/20 text-red-400"
                    }`}
                  >
                    {item.label}
                  </span>

                </div>

                <div className="text-gray-400 text-sm">

                  {new Date(item.created_at).toLocaleString()}

                </div>

              </div>

              {/* TEXT */}
              <p className="mt-5 text-gray-300 leading-relaxed">

                {item.text}

              </p>

              {/* CONFIDENCE */}
              <div className="mt-6">

                <div className="flex justify-between text-sm mb-2">

                  <span className="text-gray-400">
                    Confidence
                  </span>

                  <span className="text-cyan-400 font-semibold">
                    {item.confidence}%
                  </span>

                </div>

                <div className="w-full bg-gray-700 rounded-full h-3 overflow-hidden">

                  <div
                    className={`h-3 rounded-full ${
                      item.label === "REAL"
                        ? "bg-green-400"
                        : "bg-red-400"
                    }`}
                    style={{
                      width: `${item.confidence}%`,
                    }}
                  ></div>

                </div>

              </div>

            </div>
          ))}

        </div>
      )}

    </div>
  );
}