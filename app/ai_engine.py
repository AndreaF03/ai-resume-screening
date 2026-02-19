from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(resume_text, job_desc):
    embeddings = model.encode([resume_text, job_desc])
    score = util.cos_sim(embeddings[0], embeddings[1])
    return round(float(score[0][0]) * 100, 2)


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
