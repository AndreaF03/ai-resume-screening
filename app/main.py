from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import pdfplumber

from app.ai_engine import semantic_similarity, skill_gap

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

REQUIRED_SKILLS = ["python", "machine learning", "sql"]


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/analyze")
async def analyze(request: Request,
                  resume: UploadFile = File(...),
                  job_description: str = Form(...)):

    resume_text = extract_text_from_pdf(resume.file)

    score = semantic_similarity(resume_text, job_description)
    matched, missing = skill_gap(resume_text, REQUIRED_SKILLS)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "score": score,
            "matched": matched,
            "missing": missing
        }
    )
