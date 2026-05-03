import {
  FaReact,
  FaPython,
  FaDatabase,
  FaBrain,
  FaGithub,
  FaGlobe,
  FaShieldAlt,
  FaChartLine,
  FaRobot,
  FaLanguage,
} from "react-icons/fa";

import {
  SiFastapi,
  SiScikitlearn,
  SiTailwindcss,
  SiSqlite,
  SiVite,
} from "react-icons/si";



export default function About() {

  return (

    <div className="min-h-screen bg-[#0f172a] text-white overflow-hidden">

     {/* ========================================= */}
{/* HERO SECTION */}
{/* ========================================= */}
<section className="relative overflow-hidden py-20 md:py-24 border-b border-gray-800">

  {/* GLOW EFFECTS */}
  <div className="absolute top-0 left-0 w-[300px] md:w-[500px] h-[300px] md:h-[500px] bg-cyan-500/10 blur-3xl rounded-full"></div>

  <div className="absolute bottom-0 right-0 w-[300px] md:w-[500px] h-[300px] md:h-[500px] bg-blue-500/10 blur-3xl rounded-full"></div>

  <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-6 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 items-center">

    {/* LEFT CONTENT */}
    <div className="text-center lg:text-left">

      {/* BADGE */}
      <div className="inline-flex items-center gap-3 bg-cyan-400/10 border border-cyan-400/20 px-4 py-2 rounded-full text-cyan-300 text-xs sm:text-sm font-medium mb-6 md:mb-8 backdrop-blur-md">

        <span className="w-2 h-2 bg-cyan-400 rounded-full animate-pulse"></span>

        AI-Based Fake News Detection Platform

      </div>

      {/* TITLE */}
      <h1 className="text-3xl sm:text-4xl md:text-6xl xl:text-7xl font-extrabold leading-tight">

        About{" "}

        <span className="bg-gradient-to-r from-cyan-400 via-sky-400 to-blue-500 bg-clip-text text-transparent">
          Fake News AI
        </span>

      </h1>

      {/* DESCRIPTION */}
      <p className="mt-6 md:mt-8 text-base sm:text-lg md:text-xl text-gray-300 leading-relaxed max-w-2xl mx-auto lg:mx-0">

        Fake News AI is an intelligent AI-powered misinformation detection platform developed by 5th Year Computer Science and Engineering students as a Final Year Research Project.

        <br /><br />

        The system focuses on detecting fake and misleading Tigrigna news content using NLP, Machine Learning, and intelligent text analysis techniques.

        <br /><br />

        The platform provides real-time prediction, confidence scoring, prediction history tracking, and API integration for scalable AI analysis.

      </p>

      {/* BUTTONS */}
      <div className="mt-8 md:mt-10 flex flex-col sm:flex-row flex-wrap gap-4 sm:gap-5 justify-center lg:justify-start">

        <a
          href={`${import.meta.env.VITE_API_URL || "http://localhost:8000"}/docs`}
          target="_blank"
          rel="noreferrer"
          className="bg-cyan-400 hover:bg-cyan-500 text-black px-6 py-3 md:px-7 md:py-4 rounded-2xl font-bold transition duration-300 shadow-lg shadow-cyan-500/20 text-center"
        >
          API Docs
        </a>

        <a
          href="https://github.com/kikikatg/tigrigna_fake_news_detection_using_NLP"
          target="_blank"
          rel="noreferrer"
          className="border border-gray-600 hover:border-cyan-400 hover:text-cyan-400 px-6 py-3 md:px-7 md:py-4 rounded-2xl transition duration-300 text-center"
        >
          GitHub
        </a>

        <a
          href="https://fastapi.tiangolo.com/"
          target="_blank"
          rel="noreferrer"
          className="border border-gray-600 hover:border-cyan-400 hover:text-cyan-400 px-6 py-3 md:px-7 md:py-4 rounded-2xl transition duration-300 text-center"
        >
          FastAPI Docs
        </a>

      </div>

    </div>

    {/* RIGHT IMAGE */}
    <div className="relative flex justify-center lg:justify-end">

      {/* GLOW */}
      <div className="absolute w-[250px] sm:w-[350px] md:w-[500px] h-[250px] sm:h-[350px] md:h-[500px] bg-cyan-500/20 blur-3xl rounded-full"></div>

      <div className="absolute w-[200px] sm:w-[300px] md:w-[350px] h-[200px] sm:h-[300px] md:h-[350px] bg-blue-500/20 blur-3xl rounded-full"></div>

      <img
        src="UI2.png"
        alt="Fake News AI"
        className="relative z-10 w-[90%] sm:w-[500px] md:w-[600px] max-w-full h-auto md:h-[600px] object-contain drop-shadow-[0_0_35px_rgba(34,211,238,0.35)] hover:scale-105 transition duration-500"
      />

    </div>

  </div>

</section>

      {/* ========================================= */}
      {/* CORE FEATURES */}
      {/* ========================================= */}
      <section className="max-w-7xl mx-auto px-6 py-24">

        <div className="text-center">

          <h2 className="text-4xl md:text-5xl font-extrabold">

            Core Features

          </h2>

          <p className="mt-5 text-gray-400 text-lg max-w-3xl mx-auto">

            Advanced Artificial Intelligence capabilities designed
            for intelligent Tigrigna fake news analysis,
            real-time prediction, and research-based NLP processing.

          </p>

        </div>

        {/* FEATURE GRID */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mt-16">

          {/* FEATURE */}
          <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 hover:border-cyan-400 transition duration-300 hover:-translate-y-2">

            <FaBrain className="text-5xl text-cyan-400" />

            <h3 className="mt-6 text-2xl font-bold">
              AI Prediction
            </h3>

            <p className="mt-4 text-gray-400 leading-relaxed">

              Detects whether Tigrigna news is REAL or FAKE
              using Machine Learning classification models
              trained on NLP-based feature extraction.

            </p>

          </div>

          {/* FEATURE */}
          <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 hover:border-cyan-400 transition duration-300 hover:-translate-y-2">

            <FaDatabase className="text-5xl text-cyan-400" />

            <h3 className="mt-6 text-2xl font-bold">
              History Storage
            </h3>

            <p className="mt-4 text-gray-400 leading-relaxed">

              Stores prediction history in SQLite database
              with timestamps, prediction labels,
              and confidence score tracking.

            </p>

          </div>

          {/* FEATURE */}
          <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 hover:border-cyan-400 transition duration-300 hover:-translate-y-2">

            <FaGlobe className="text-5xl text-cyan-400" />

            <h3 className="mt-6 text-2xl font-bold">
              Real-Time Analysis
            </h3>

            <p className="mt-4 text-gray-400 leading-relaxed">

              FastAPI backend provides real-time prediction
              processing and fast AI response handling
              through RESTful API architecture.

            </p>

          </div>

          {/* FEATURE */}
          <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 hover:border-cyan-400 transition duration-300 hover:-translate-y-2">

            <FaLanguage className="text-5xl text-cyan-400" />

            <h3 className="mt-6 text-2xl font-bold">
              Intelligent NLP Engine
            </h3>

            <p className="mt-4 text-gray-400 leading-relaxed">

              Advanced Natural Language Processing pipeline
              performs preprocessing, tokenization,
              normalization, and intelligent feature extraction.

            </p>

          </div>

          {/* FEATURE */}
          <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 hover:border-cyan-400 transition duration-300 hover:-translate-y-2">

            <FaChartLine className="text-5xl text-cyan-400" />

            <h3 className="mt-6 text-2xl font-bold">
              Confidence Scoring
            </h3>

            <p className="mt-4 text-gray-400 leading-relaxed">

              Displays AI confidence percentage with
              visual progress indicators for
              transparent and explainable prediction analysis.

            </p>

          </div>

          {/* FEATURE */}
          <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 hover:border-cyan-400 transition duration-300 hover:-translate-y-2">

            <FaShieldAlt className="text-5xl text-cyan-400" />

            <h3 className="mt-6 text-2xl font-bold">
              Secure API Architecture
            </h3>

            <p className="mt-4 text-gray-400 leading-relaxed">

              Modern FastAPI architecture provides
              scalable backend services, secure
              frontend-backend communication, and clean API routing.

            </p>

          </div>

        </div>

      </section>
{/* ========================================= */}
{/* PROJECT OBJECTIVES */}
{/* ========================================= */}
<section className="bg-[#111827] border-y border-gray-800">

  <div className="max-w-7xl mx-auto px-6 py-24">

    <div className="text-center">

      <h2 className="text-4xl md:text-5xl font-extrabold">
        Project Objectives
      </h2>

      <p className="mt-5 text-gray-400 text-lg max-w-3xl mx-auto">
        Main goals and research objectives behind the development
        of the AI-powered Tigrigna fake news detection system.
      </p>

    </div>

    {/* GRID */}
    <div className="grid md:grid-cols-2 gap-8 mt-16">

      {/* CARD */}
      <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
        hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
        transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

        <h3 className="text-2xl font-bold text-cyan-400">
          Combat Misinformation
        </h3>

        <p className="mt-4 text-gray-400 leading-relaxed">
          Reduce the spread of fake and misleading Tigrigna news
          using intelligent AI-powered verification systems.
        </p>

      </div>

      {/* CARD */}
      <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
        hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
        transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

        <h3 className="text-2xl font-bold text-cyan-400">
          Support Low-Resource Languages
        </h3>

        <p className="mt-4 text-gray-400 leading-relaxed">
          Build NLP solutions for underrepresented languages like Tigrigna
          using modern machine learning techniques.
        </p>

      </div>

      {/* CARD */}
      <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
        hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
        transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

        <h3 className="text-2xl font-bold text-cyan-400">
          Real-Time Prediction
        </h3>

        <p className="mt-4 text-gray-400 leading-relaxed">
          Provide instant classification of news content using
          a real-time AI web application system.
        </p>

      </div>

      {/* CARD */}
      <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
        hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
        transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

        <h3 className="text-2xl font-bold text-cyan-400">
          AI Research Contribution
        </h3>

        <p className="mt-4 text-gray-400 leading-relaxed">
          Contribute to research in NLP, misinformation detection,
          and AI applications for African languages.
        </p>

      </div>

    </div>

  </div>
</section>
      {/* ========================================= */}
{/* TECHNOLOGIES */}
{/* ========================================= */}
<section className="max-w-7xl mx-auto px-6 py-24">

  <div className="text-center">

    <h2 className="text-4xl md:text-5xl font-extrabold">
      Technologies Used
    </h2>

    <p className="mt-5 text-gray-400 text-lg max-w-3xl mx-auto">
      Modern frontend, backend, AI, and database technologies powering the system.
    </p>

  </div>

  {/* GRID */}
  <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mt-16">

    {/* CARD */}
    <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
      hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
      transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

      <FaReact className="text-5xl text-cyan-400" />

      <h3 className="mt-5 text-2xl font-bold">React + Vite</h3>

      <p className="mt-3 text-gray-400">
        Fast and modern frontend framework for responsive UI.
      </p>

    </div>

    {/* CARD */}
    <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
      hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
      transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

      <SiFastapi className="text-5xl text-cyan-400" />

      <h3 className="mt-5 text-2xl font-bold">FastAPI</h3>

      <p className="mt-3 text-gray-400">
        High-performance Python API for AI prediction system.
      </p>

    </div>

    {/* CARD */}
    <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
      hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
      transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

      <SiScikitlearn className="text-5xl text-cyan-400" />

      <h3 className="mt-5 text-2xl font-bold">Scikit-Learn</h3>

      <p className="mt-3 text-gray-400">
        Machine learning library for training classification models.
      </p>

    </div>

    {/* CARD */}
    <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
      hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
      transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

      <FaBrain className="text-5xl text-cyan-400" />

      <h3 className="mt-5 text-2xl font-bold">NLP Processing</h3>

      <p className="mt-3 text-gray-400">
        Text preprocessing and language understanding pipeline.
      </p>

    </div>

    {/* CARD */}
    <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
      hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
      transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

      <FaDatabase className="text-5xl text-cyan-400" />

      <h3 className="mt-5 text-2xl font-bold">SQLite Database</h3>

      <p className="mt-3 text-gray-400">
        Stores prediction history with timestamps and confidence.
      </p>

    </div>

    {/* CARD */}
    <div className="bg-[#111827] border border-gray-700 rounded-3xl p-8 
      hover:border-cyan-400 hover:shadow-lg hover:shadow-cyan-500/10 
      transition-all duration-300 hover:-translate-y-2 hover:scale-[1.02]">

      <SiTailwindcss className="text-5xl text-cyan-400" />

      <h3 className="mt-5 text-2xl font-bold">Tailwind CSS</h3>

      <p className="mt-3 text-gray-400">
        Utility-first styling for modern responsive UI design.
      </p>

    </div>

  </div>

</section>
      {/* ========================================= */}
      {/* AI WORKFLOW */}
      {/* ========================================= */}
      <section className="bg-[#111827] border-y border-gray-800">

        <div className="max-w-7xl mx-auto px-6 py-24">

          <div className="text-center">

            <h2 className="text-4xl md:text-5xl font-extrabold">

              How The AI Works

            </h2>

            <p className="mt-5 text-gray-400 text-lg max-w-3xl mx-auto">

              Intelligent Machine Learning workflow behind
              the fake news detection system.

            </p>

          </div>

          {/* STEPS */}
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mt-16">

            {[
              "Input News Text",
              "Text Preprocessing",
              "TF-IDF Vectorization",
              "AI Prediction Result",
            ].map((step, index) => (

              <div
                key={index}
                className="bg-[#0f172a] border border-gray-700 rounded-3xl p-8 text-center hover:border-cyan-400 transition"
              >

                <div className="w-16 h-16 mx-auto rounded-full bg-cyan-400 text-black flex items-center justify-center text-2xl font-extrabold">

                  {index + 1}

                </div>

                <h3 className="mt-6 text-xl font-bold">

                  {step}

                </h3>

              </div>

            ))}

          </div>

        </div>

      </section>

      {/* ========================================= */}
      {/* FOOTER */}
      {/* ========================================= */}
      <section className="border-t border-gray-800">

        <div className="max-w-7xl mx-auto px-6 py-12 text-center">

          <p className="text-gray-400 text-lg leading-relaxed max-w-4xl mx-auto">

            Developed by 5th Year Computer Science and Engineering Students
            as a Final Year Artificial Intelligence Research Project
            focusing on Tigrigna Fake News Detection using
            NLP and Machine Learning technologies.

          </p>

          {/* ICONS */}
          <div className="mt-8 flex justify-center gap-8 text-3xl">

            <a
              href="https://github.com/kikikatg/tigrigna_fake_news_detection_using_NLP"
              target="_blank"
              rel="noreferrer"
              className="hover:text-cyan-400 transition duration-300"
            >
              <FaGithub />
            </a>

            <a
              href="https://www.python.org/"
              target="_blank"
              rel="noreferrer"
              className="hover:text-cyan-400 transition duration-300"
            >
              <FaPython />
            </a>

            <a
              href="https://react.dev/"
              target="_blank"
              rel="noreferrer"
              className="hover:text-cyan-400 transition duration-300"
            >
              <FaReact />
            </a>

            <a
              href="https://vitejs.dev/"
              target="_blank"
              rel="noreferrer"
              className="hover:text-cyan-400 transition duration-300"
            >
              <SiVite />
            </a>

          </div>

          {/* COPYRIGHT */}
          <p className="mt-8 text-gray-500">

            © 2026 Fake News AI — Final Year CSE Project

          </p>

        </div>

      </section>

    </div>
  );
}