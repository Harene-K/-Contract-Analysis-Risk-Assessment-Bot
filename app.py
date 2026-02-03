import streamlit as st

from utils.pdf_exporter import generate_pdf
from utils.file_loader import extract_text
from utils.language_handler import detect_and_normalize
from utils.clause_extractor import extract_clauses
from utils.ner_extractor import extract_entities
from utils.risk_rules import assess_risks, calculate_contract_risk
from llm.legal_reasoning import analyze_clause

st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.write("Upload a contract to analyze legal risks in simple language.")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    with st.spinner("Analyzing contract..."):
        raw_text = extract_text(uploaded_file)
        normalized_text, language = detect_and_normalize(raw_text)
        clauses = extract_clauses(normalized_text)
        entities = extract_entities(normalized_text)
        risk_results = assess_risks(clauses)

        contract_score, contract_level = calculate_contract_risk(risk_results)

    st.success(f"Language detected: {language}")

    st.subheader("📊 Overall Contract Risk")
    st.metric("Risk Level", contract_level, contract_score)

    st.subheader("📌 Key Entities")
    st.json(entities)

    st.subheader("📑 Clause Analysis")
    for clause in clauses:
        risk = risk_results.get(clause["id"], "Low")
        explanation, suggestion = analyze_clause(clause["text"])

        with st.expander(f"Clause {clause['id']} — Risk: {risk}"):
            st.write("**Original Clause**")
            st.write(clause["text"])

            st.write("**Plain English Explanation**")
            st.write(explanation)

            if suggestion:
                st.write("**Suggested Safer Alternative**")
                st.write(suggestion)
    if st.button("Download Risk Report as PDF"):
        pdf_filename = "contract_risk_report.pdf"
        summary = f"Overall Risk Level: {contract_level}\n\nKey Entities:\n"
        for key, vals in entities.items():
            summary += f"- {key}: {', '.join(vals) if vals else 'N/A'}\n"

        clause_texts = [clause["text"] for clause in clauses]
        generate_pdf(pdf_filename, summary, contract_level, clause_texts)

        with open(pdf_filename, "rb") as f:
            st.download_button(
                label="Download PDF",
                data=f,
                file_name=pdf_filename,
                mime="application/pdf"
            )

st.markdown("---")
st.caption("⚠️ Informational tool only. Not legal advice.")
