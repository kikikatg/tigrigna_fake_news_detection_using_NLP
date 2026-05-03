import { useState } from "react";
import { NavLink, Link } from "react-router-dom";
import { FaNewspaper } from "react-icons/fa";
import { HiMenuAlt3, HiX } from "react-icons/hi";

function Navbar() {

  const [open, setOpen] = useState(false);

  const navItems = [
    { name: "Home", path: "/" },
    { name: "History", path: "/history" },
    { name: "About", path: "/about" },
  ];

  return (
    <nav className="sticky top-0 z-50 backdrop-blur-2xl bg-[#040a18]/95 border-b border-cyan-500/10 shadow-lg shadow-black/30">

      {/* TOP GLOW LINE */}
      <div className="absolute bottom-0 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-cyan-500/40 to-transparent"></div>

      <div className="max-w-7xl mx-auto px-10 py-8 flex items-center justify-between">

        {/* LOGO */}
        <Link to="/" className="flex items-center gap-3 group">

          <div className="bg-cyan-400/10 p-3 rounded-xl border border-cyan-400/20 group-hover:scale-105 transition">
            <FaNewspaper className="text-cyan-400 text-2xl" />
          </div>

          <div>
            <h1 className="text-2xl font-extrabold tracking-wide">
              <span className="text-white">Fake</span>
              <span className="bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                News AI
              </span>
            </h1>

            <p className="text-xs text-gray-400">
              Tigrigna Detection System
            </p>
          </div>

        </Link>

        {/* DESKTOP MENU */}
        <div className="hidden md:flex items-center gap-14 text-[20px] font-medium">

          {navItems.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              className={({ isActive }) =>
                `relative pb-2 transition duration-300 hover:text-cyan-400 ${
                  isActive
                    ? "text-cyan-400 after:absolute after:left-0 after:-bottom-1 after:w-full after:h-[2px] after:bg-gradient-to-r after:from-cyan-400 after:to-blue-500"
                    : "text-gray-300"
                }`
              }
            >
              {item.name}
            </NavLink>
          ))}

        </div>

        {/* MOBILE BUTTON */}
        <button
          className="md:hidden text-2xl text-cyan-400"
          onClick={() => setOpen(!open)}
        >
          {open ? <HiX /> : <HiMenuAlt3 />}
        </button>

      </div>

      {/* MOBILE MENU */}
      {open && (
        <div className="md:hidden px-6 pb-6 flex flex-col gap-5 bg-[#040a18] border-t border-cyan-500/10">

          {navItems.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              onClick={() => setOpen(false)}
              className={({ isActive }) =>
                `py-2 transition ${
                  isActive ? "text-cyan-400" : "text-gray-300"
                }`
              }
            >
              {item.name}
            </NavLink>
          ))}

        </div>
      )}

    </nav>
  );
}

export default Navbar;