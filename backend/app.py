import json
import os
from flask import Flask, request, jsonify
from resume_utils import (
    extract_text_from_pdf_bytes,
    extract_text_from_docx_bytes,
    extract_text_from_txt_bytes,
    normalize_text,
    detect_skills,
    extract_candidates_using_spacy,
    compute_similarity_score,
    compare_skills,
    simple_suggestions,
    )


app = Flask(__name__)


# Load skills list
SKILLS_FILE = os.path.join(os.path.dirname(__file__), "skills.json")
with open(SKILLS_FILE, "r", encoding="utf-8") as f:
    SKILLS_LIST = json.load(f)




@app.route("/health")
def health():
    return jsonify({"status": "ok"})




@app.route("/analyze", methods=["POST"])
def analyze():
    # expects multipart form: resume file (file), optional jd_text (text)
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    f = request.files["file"]
    filename = f.filename.lower()
    data = f.read()


    if filename.endswith(".pdf"):
            raw_text = extract_text_from_pdf_bytes(data)
    elif filename.endswith(".docx") or filename.endswith(".doc"):
     raw_text = extract_text_from_docx_bytes(data)
    else:
        raw_text = extract_text_from_txt_bytes(data)


    raw_text = normalize_text(raw_text)


    # detect skills using dictionary
    found_skills = detect_skills(raw_text, SKILLS_LIST)


    # also extract candidate phrases using spaCy (optional)
    candidates = extract_candidates_using_spacy(raw_text)


    # job description
    jd_text = request.form.get("jd_text", "")
    jd_skills = []
    similarity = None
    comp = None
    suggestions = []


    if jd_text:
        jd_text = normalize_text(jd_text)
        # naive skills: match against skills list
        jd_skills = detect_skills(jd_text, SKILLS_LIST)
        similarity = compute_similarity_score(raw_text, jd_text)
        comp = compare_skills(found_skills, jd_skills)
        suggestions = simple_suggestions(comp.get("missing", []))


    response = {
    "found_skills": found_skills,
    "candidate_phrases": candidates,
    "jd_skills": jd_skills,
    "similarity": similarity,
    "comparison": comp,
    "suggestions": suggestions,
    }
    return jsonify(response)




if __name__ == "__main__":
    app.run(debug=True)