import { useNavigate } from "react-router-dom";

export default function Hero() {

  const navigate = useNavigate();

  const handleStartDetection = () => {
    const section = document.getElementById("predict-section");
    if (section) section.scrollIntoView({ behavior: "smooth" });
  };

  const handleLearnMore = () => {
    navigate("/about");
  };

  return (
    <section className="relative overflow-hidden py-24">

      {/* BACKGROUND GLOW */}
      <div className="absolute top-0 left-0 w-96 h-96 bg-cyan-500/10 blur-3xl rounded-full"></div>
      <div className="absolute bottom-0 right-0 w-96 h-96 bg-blue-500/10 blur-3xl rounded-full"></div>

      <div className="relative max-w-7xl mx-auto px-6 grid lg:grid-cols-2 gap-20 items-center">

        {/* LEFT SIDE */}
        <div>

          {/* BADGE */}
          <div className="inline-flex items-center gap-3 bg-cyan-400/10 border border-cyan-400/20 px-5 py-2 rounded-full text-cyan-300 text-sm font-medium mb-8 backdrop-blur-md">

            <span className="w-2.5 h-2.5 bg-cyan-400 rounded-full animate-pulse"></span>

            AI-Powered Fake News Detection System

          </div>

          {/* HEADING — NOW BALANCED (3 LINES) */}
          <h1 className="text-4xl md:text-5xl xl:text-6xl font-extrabold leading-tight tracking-tight">

            Detect{" "}
            <span className="bg-gradient-to-r from-cyan-400 via-sky-400 to-blue-500 bg-clip-text text-transparent">
              Fake News
            </span>
            <br />

            in{" "}
            <span className=" bg-gradient-to-r from-cyan-400 via-sky-400 to-blue-500 bg-clip-text text-transparent">
              Tigrigna Language
            </span>
            <br />

            Instantly with AI

          </h1>

          {/* DESCRIPTION */}
          <p className="mt-8 text-lg md:text-xl text-gray-300 leading-relaxed max-w-2xl">

            Advanced NLP and Machine Learning system
            for identifying fake and real Tigrigna news
            articles with intelligent preprocessing,
            confidence scoring, and real-time AI analysis.

          </p>

          {/* CTA BUTTONS */}
          <div className="mt-12 flex flex-wrap gap-5">

            <button
              onClick={handleStartDetection}
              className="bg-cyan-400 hover:bg-cyan-500 text-black font-bold px-8 py-4 rounded-2xl transition duration-300 shadow-lg shadow-cyan-500/20 hover:scale-105"
            >
              Start Detection
            </button>

            <button
              onClick={handleLearnMore}
              className="border border-gray-600 hover:border-cyan-400 hover:text-cyan-400 px-8 py-4 rounded-2xl transition duration-300 hover:bg-cyan-400/5"
            >
              Learn More
            </button>

          </div>

          {/* STATS */}
          <div className="mt-16 flex flex-wrap gap-12">

            <div>
              <h2 className="text-4xl font-extrabold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                95.6%
              </h2>
              <p className="text-gray-400 mt-2">Detection Accuracy</p>
            </div>

            <div>
              <h2 className="text-4xl font-extrabold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                AI
              </h2>
              <p className="text-gray-400 mt-2">NLP Powered</p>
            </div>

            <div>
              <h2 className="text-4xl font-extrabold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                24/7
              </h2>
              <p className="text-gray-400 mt-2">Real-Time Analysis</p>
            </div>

          </div>

        </div>

        {/* RIGHT SIDE IMAGE — BIGGER */}
        <div className="relative flex justify-center">

          <div className="absolute w-[650px] h-[650px] bg-cyan-500/20 blur-3xl rounded-full"></div>
          <div className="absolute w-[450px] h-[450px] bg-blue-500/20 blur-3xl rounded-full"></div>

          <img
            src="/UI1.png"
            alt="Fake News AI"
            className="relative z-10 w-full max-w-4xl h-[560px] object-contain 
            drop-shadow-[0_0_50px_rgba(34,211,238,0.35)] 
            hover:scale-110 transition duration-500"
          />

        </div>

      </div>

    </section>
  );
}