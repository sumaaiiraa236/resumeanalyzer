Resume Analyzer
Resume Analyzer is an AI-powered web application that extracts, analyzes, and scores skills from resumes.
Designed with a modern pastel theme (Sorbet Stem, Petal Glaze, Dusty Orchid, Lilac Grey), it provides recruiters and job seekers with an elegant way to evaluate resumes.

✨ Features

📂 Upload resumes in PDF/DOCX format

🤖 AI-based skill extraction with NLP (spaCy + Sentence Transformers)

📊 Smart scoring system with progress bar visualizations

🎨 Beautiful UI inspired by modern event sites

📱 Responsive design (works seamlessly on desktop & mobile)

⚡ Fast and lightweight (Flask + React + Tailwind)

🛠️ Tech Stack

Frontend

React (with Hooks)

Tailwind CSS (custom pastel theme)

Framer Motion (smooth animations)

Backend

Flask (REST API)

pdfplumber, python-docx (resume parsing)

spaCy + Sentence Transformers (NLP & embeddings)

📂 Project Structure
ResumeAnalyser/
│── resume/
│   ├── backend/         # Flask server + NLP logic
│   │   ├── app.py
│   │   ├── resume_utils.py
│   │   └── requirements.txt
│   │
│   └── frontend/        # React + Tailwind UI
│       ├── src/
│       │   ├── components/
│       │   │   ├── Navbar.js
│       │   │   ├── UploadSection.js
│       │   │   ├── Results.js
│       │   │   └── Footer.js
│       │   └── App.js
│       └── package.json
│
└── README.md

⚡ Getting Started
1️⃣ Clone the Repository
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

2️⃣ Backend Setup
cd resume/backend
conda create -n resume_env python=3.10 -y
conda activate resume_env
pip install -r requirements.txt
python app.py


➡️ Runs at http://localhost:5000

3️⃣ Frontend Setup
cd ../frontend
npm install
npm start


➡️ Runs at http://localhost:3000

🎯 Usage

Launch the frontend in browser

Upload a resume (PDF or DOCX)

Backend extracts skills → calculates scores

View results as progress bars in pastel colors

📸 Screenshots
Upload Page

(insert screenshot here)

Results Page

(insert screenshot here)

🌟 Roadmap

 Add Job Description Matching (compare resume to JD)

 Export results as PDF report

 Add multi-language resume support

 Career recommendations powered by AI

🤝 Contributing

Contributions are welcome! 🎉

Fork the repo

Create your feature branch (git checkout -b feature/new-feature)

Commit changes (git commit -m 'Add new feature')

Push to branch (git push origin feature/new-feature)

Open a Pull Request 🚀
