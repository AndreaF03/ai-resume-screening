from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def semantic_similarity(resume_text, job_desc):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(float(similarity[0][0]) * 100, 2)


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
