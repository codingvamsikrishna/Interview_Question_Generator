from skills_db import SKILL_DB

question_bank = {

    "python": [
        "Explain list vs tuple in Python.",
        "What is PEP 8?",
        "What is a decorator?"
    ],

    "java": [
        "What is JVM?",
        "Explain OOPS concepts.",
        "What is inheritance?"
    ],

    "sql": [
        "What is normalization?",
        "Difference between primary key and foreign key?",
        "What is JOIN and its types?"
    ],

    "machine learning": [
        "What is Machine Learning?",
        "Explain bias-variance tradeoff.",
        "What is overfitting?"
    ],

    "javascript":[
        "What is DOM?",
        "Difference between var, let, const?",
        "What is hoisting?"
    ],

    "html": [
        "What is HTML?",
        "What are semantic tags?",
        "Difference between div and span?"
    ],

    "css": [
        "What is CSS?",
        "What is Flexbox?",
        "Difference between margin and padding?"
    ],
}

def extract_skills(text):
    text = text.lower()
    extracted = []

    for skill in SKILL_DB:
        if skill in text:
            extracted.append(skill)

    return extracted

def generate_questions(skills):
    questions = []

    for skill in skills:
        if skill in question_bank:
            questions.extend(question_bank[skill])

    return questions
