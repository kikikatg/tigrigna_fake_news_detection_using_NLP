import {
  FaGithub,
  FaLinkedin,
  FaEnvelope,
} from "react-icons/fa";

export default function Footer() {

  return (

    <footer className="w-full mt-36 border-t border-gray-800 bg-[#0b1120]">

      {/* FULL WIDTH BACKGROUND CONTAINER */}
      <div className="w-full">

        {/* CENTERED CONTENT INSIDE */}
        <div className="max-w-7xl mx-auto px-6 py-14">

          <div className="grid md:grid-cols-3 gap-12">

            {/* LEFT */}
            <div>

              <h2 className="text-3xl font-extrabold bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">

                Fake News AI

              </h2>

              <p className="mt-5 text-gray-400 leading-relaxed">

                AI-powered Tigrigna fake news detection system using Natural Language Processing and Machine Learning technologies.

              </p>

            </div>

            {/* CENTER */}
            <div>

              <h3 className="text-xl font-bold text-white mb-5">

                Quick Links

              </h3>

              <div className="flex flex-col gap-3 text-gray-400">

                <a href="/" className="hover:text-cyan-400 transition">
                  Home
                </a>

                <a href="/history" className="hover:text-cyan-400 transition">
                  History
                </a>

                <a href="/about" className="hover:text-cyan-400 transition">
                  About
                </a>

              </div>

            </div>

            {/* RIGHT */}
            <div>

              <h3 className="text-xl font-bold text-white mb-5">

                Connect

              </h3>

              <div className="flex gap-5 text-2xl text-gray-400">

                {/* GITHUB */}
                <a
                  href="https://github.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hover:text-cyan-400 transition"
                >
                  <FaGithub />
                </a>

                {/* LINKEDIN */}
                <a
                  href="https://www.linkedin.com/in/kiros-asefa/"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hover:text-cyan-400 transition"
                >
                  <FaLinkedin />
                </a>

                {/* EMAIL */}
                <a
                  href="#"
                  onClick={(e) => {
                    e.preventDefault();

                    const email = "kikikatg@email.com";
                    const subject = "Fake News AI Project";
                    const body = "Hello Kiros,%0D%0A%0D%0AI am interested in your project.";

                    const mailtoLink = `mailto:${email}?subject=${subject}&body=${body}`;

                    window.location.href = mailtoLink;
                  }}
                  className="hover:text-cyan-400 transition"
                >
                  <FaEnvelope />
                </a>

              </div>

            </div>

          </div>

          {/* BOTTOM */}
          <div className="border-t border-gray-800 mt-12 pt-6 text-center text-gray-500 text-sm">

            © 2026 Fake News AI — Built with React, FastAPI & Machine Learning.

          </div>

        </div>

      </div>

    </footer>
  );
}