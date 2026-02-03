RISK_KEYWORDS = {
    "High": [
        "indemnify",
        "penalty",
        "liable",
        "terminate immediately",
        "non-compete"
    ],
    "Medium": [
        "terminate",
        "jurisdiction",
        "arbitration",
        "auto-renew"
    ]
}

def assess_risks(clauses):
    risk_scores = {}

    for clause in clauses:
        text = clause["text"].lower()
        risk = "Low"

        for level, keywords in RISK_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                risk = level
                break

        risk_scores[clause["id"]] = risk

    return risk_scores


def calculate_contract_risk(risk_results):
    score_map = {"Low": 1, "Medium": 2, "High": 3}

    total = sum(score_map[r] for r in risk_results.values())
    avg = round(total / len(risk_results), 2)

    if avg <= 1.5:
        level = "Low"
    elif avg <= 2.2:
        level = "Medium"
    else:
        level = "High"

    return avg, level
