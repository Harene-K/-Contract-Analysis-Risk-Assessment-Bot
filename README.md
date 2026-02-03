# Contract Analysis & Risk Assessment Bot

## Problem
Small and Medium Enterprises (SMEs) often sign complex legal contracts without
fully understanding risks such as penalties, indemnities, or IP ownership loss.

## Solution
A GenAI-powered legal assistant that analyzes contracts to:
- Extract clauses
- Identify legal risks
- Explain clauses in simple business language
- Generate a contract-level risk score
- Export a PDF risk report

## Features
- Clause-level risk detection
- Contract-level risk scoring
- Entity extraction (parties, dates, money)
- Plain-language explanations
- PDF export
- Confidential local processing

## Tech Stack
- Python
- Streamlit
- spaCy
- Rule-based legal risk engine
- ReportLab

## How to Run
pip install -r requirements.txt
streamlit run app.py

## Disclaimer
This tool provides informational insights only and does not replace legal advice.
