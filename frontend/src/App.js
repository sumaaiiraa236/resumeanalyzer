import React, { useState } from "react";
import Navbar from "./components/Navbar";
import UploadSection from "./components/UploadSection";
import Results from "./components/Results";
import Footer from "./components/Footer";
import "./App.css";
import bgImage from "./assets/download-5.jpg";

function App() {
  const [results, setResults] = useState(null);

  return (
    <div
      className="bg-lilacGrey min-h-screen flex flex-col"
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        minHeight: "100vh",
        width: "100vw",
        overflowX: "hidden",
      }}
    >
      <Navbar />
      <main className="flex-1">
        {!results ? (
          <UploadSection onAnalyze={setResults} />
        ) : (
          <Results data={results} />
        )}
      </main>
      <Footer />
    </div>
  );
}

export default App;
