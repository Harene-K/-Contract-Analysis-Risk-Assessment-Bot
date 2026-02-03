def analyze_clause(text):
    explanation = (
        "This clause defines responsibilities or conditions that may "
        "affect one or both parties."
    )

    suggestion = None
    if "penalty" in text.lower():
        suggestion = "Consider negotiating a capped or mutually applicable penalty clause."

    if "indemnify" in text.lower():
        suggestion = "Limit indemnity scope and add reciprocal protection."

    return explanation, suggestion
