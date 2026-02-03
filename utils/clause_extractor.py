import re

def extract_clauses(text):
    raw_clauses = re.split(r"\n\s*\d+\.\s*", text)
    clauses = []

    for i, clause in enumerate(raw_clauses):
        if clause.strip():
            clauses.append({
                "id": i + 1,
                "text": clause.strip()
            })

    return clauses
