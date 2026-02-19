from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def calculate_similarity(resume_text, job_desc):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(float(similarity[0][0]) * 100, 2)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze(request: Request,
                  resume: UploadFile = File(...),
                  job_description: str = Form(...)):

    resume_text = extract_text_from_pdf(resume.file)
    score = calculate_similarity(resume_text, job_description)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "score": score}
    )
