function Navbar() {
  return (
    <nav className="bg-dustyOrchid text-white px-6 py-4 flex justify-between items-center shadow-md">
      <h1 className="text-xl font-bold">Resume Analyzer</h1>
      <button className="bg-sorbetStem text-black px-4 py-2 rounded-lg hover:bg-petalGlaze transition">
        Home
      </button>
    </nav>
  );
}

export default Navbar;
