import { motion } from "framer-motion";

function UploadSection({ onAnalyze }) {
  return (
    <section className="flex flex-col items-center justify-center mt-10">
      <motion.h2
        className="text-3xl font-bold text-pink-600 mb-2"
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
      >
        Upload Your Resume
      </motion.h2>
      <motion.p
        className="text-gray-600 mb-6"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5, duration: 1 }}
      >
        Get instant insights about your skills and strengths.
      </motion.p>
      {/* Your upload box here */}
    </section>
  );
}
export default UploadSection;