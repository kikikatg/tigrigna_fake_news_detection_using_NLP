import Hero from "../components/Hero";
import PredictionForm from "../components/PredictionForm";
import Footer from "../components/Footer";

function Home() {
  return (
    <div>

      {/* HERO */}
      <Hero />

      {/* PREDICTION SECTION */}
      <div className="max-w-5xl mx-auto px-6 pb-20">

        <PredictionForm />
        <Footer />

      </div>

    </div>
  );
}

export default Home;