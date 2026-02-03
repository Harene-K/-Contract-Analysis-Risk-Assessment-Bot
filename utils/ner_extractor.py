import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "Parties": set(),
        "Dates": set(),
        "Amounts": set(),
        "Locations": set()
    }

    blacklist = {"client", "service provider", "party", "parties"}

    for ent in doc.ents:
        value = ent.text.strip()

        if ent.label_ in ["ORG", "PERSON"]:
            entities["Parties"].add(value)

        elif ent.label_ == "DATE":
            entities["Dates"].add(value)

        elif ent.label_ == "MONEY":
            entities["Amounts"].add(value)

        elif ent.label_ in ["GPE", "LOC"]:
            if value.lower() not in blacklist:
                entities["Locations"].add(value)

    # Convert sets back to lists for JSON display
    return {k: list(v) for k, v in entities.items()}
