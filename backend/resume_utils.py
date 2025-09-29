import io
import json
import re
from typing import List


import pdfplumber
import docx
import spacy
from sentence_transformers import SentenceTransformer, util
from typing import List


import pdfplumber
import docx
import spacy
from sentence_transformers import SentenceTransformer, util


# Load spaCy model (small) and sentence-transformers model lazily
_nlp = None
_sbert = None


def get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("en_core_web_sm")
    return _nlp
def get_sbert():
    global _sbert
    if _sbert is None:
        _sbert = SentenceTransformer("all-MiniLM-L6-v2")
    return _sbert
def extract_text_from_pdf_bytes(file_bytes: bytes) -> str:
    text_pages = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:    
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text_pages.append(page_text)
    return "\n".join(text_pages)
def extract_text_from_docx_bytes(file_bytes: bytes) -> str:
    doc = docx.Document(io.BytesIO(file_bytes))
    paragraphs = [p.text for p in doc.paragraphs]
    return "\n".join(paragraphs)
def extract_text_from_txt_bytes(file_bytes: bytes) -> str:
    return file_bytes.decode(errors="ignore")




def normalize_text(text: str) -> str:
# simple normalization
    text = re.sub(r"\s+", " ", text)
    return text.strip()




def detect_skills(text: str, skills_list: List[str]) -> List[str]:
    text_low = text.lower()
    found = set()
    for skill in skills_list:
        s = skill.lower()
# simple contains match or word boundary
        if s in text_low:
            found.add(skill)
        else:
# try fuzzy token match using simple tokenization
            if " " in s:
                if s in text_low:
                    found.add(skill)
    return sorted(found)
def extract_candidates_using_spacy(text: str, top_k: int = 30) -> List[str]:
    nlp = get_nlp()
    doc = nlp(text)
# extract noun chunks and entities as candidate skills
    candidates = set()
    for chunk in doc.noun_chunks:
        if len(chunk.text.split()) <= 5:
            candidates.add(chunk.text.strip())
    for ent in doc.ents:
        candidates.add(ent.text.strip())
# simple cleanup
    cleaned = [c for c in candidates if len(c) > 1]
    return cleaned[:top_k]




def embed_texts(texts: List[str]):
    model = get_sbert()
    return model.encode(texts, convert_to_tensor=True)




def compute_similarity_score(resume_text: str, jd_text: str) -> float:
    model = get_sbert()
    emb_res = model.encode(resume_text, convert_to_tensor=True)
    emb_jd = model.encode(jd_text, convert_to_tensor=True)
    sim = util.cos_sim(emb_res, emb_jd).item()
# normalize to percentage 0-100
    return round(float(sim) * 100, 2)
def compare_skills(resume_skills: List[str], jd_skills: List[str]) -> dict:
    resume_set = set([s.lower() for s in resume_skills])
    jd_set = set([s.lower() for s in jd_skills])
    matched = [s for s in resume_skills if s.lower() in jd_set]
    missing = [s for s in jd_skills if s.lower() not in resume_set]
    coverage = 0.0
    if len(jd_skills) > 0:
        coverage = round(len(matched) / len(jd_skills) * 100, 2)
    return {"matched": matched, "missing": missing, "coverage": coverage}




def simple_suggestions(missing_skills: List[str]) -> List[str]:
    suggestions = []
    for s in missing_skills[:10]:
        suggestions.append(f"Consider adding experience or projects that show: {s}")
    if not suggestions:
        suggestions.append("Resume already contains many JD skills. Consider emphasizing achievements and metrics.")
    return suggestions