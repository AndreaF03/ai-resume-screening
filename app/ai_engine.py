import spacy

# Load model once (important)
nlp = spacy.load("en_core_web_sm")


def semantic_similarity(resume_text, job_desc):
    doc1 = nlp(resume_text)
    doc2 = nlp(job_desc)

    # If either document is empty, avoid crash
    if not doc1.vector_norm or not doc2.vector_norm:
        return 0.0

    return round(doc1.similarity(doc2) * 100, 2)


def skill_gap(resume_text, required_skills):
    resume_lower = resume_text.lower()

    matched = []
    missing = []

    for skill in required_skills:
        if skill.lower() in resume_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing
