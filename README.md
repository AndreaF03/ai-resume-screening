#  AI-Powered Resume Screening

An NLP-based web application that compares resumes with job descriptions and generates a similarity score.

##  Features
- Resume PDF Upload
- NLP Text Extraction
- TF-IDF Similarity
- Cosine Similarity Matching
- Match Percentage Output

##  Tech Stack
- FastAPI
- Scikit-learn
- spaCy
- PDFPlumber
- Jinja2

## Deployment
Deployed on Render.

##  Run Locally
pip install -r requirements.txt
uvicorn app.main:app --reload

##  Upgrade v2.0 – Semantic AI Version

New Features:
- Sentence Embedding Similarity (MiniLM)
- Skill Gap Detection
- Improved Ranking Accuracy
