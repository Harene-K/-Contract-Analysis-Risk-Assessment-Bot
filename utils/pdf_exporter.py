from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def clean_text(text):
    return text.replace("“", '"').replace("”", '"').replace("’", "'")

def generate_pdf(filename, summary, risk_level, clauses):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, "Contract Risk Assessment Report")

    y -= 30
    c.setFont("Helvetica", 11)
    c.drawString(40, y, f"Overall Risk Level: {risk_level}")

    y -= 30
    c.drawString(40, y, "Summary:")
    y -= 20

    text = c.beginText(40, y)
    for line in summary.split("\n"):
        text.textLine(line)
    c.drawText(text)

    y = text.getY() - 30
    c.drawString(40, y, "Clauses:")

    y -= 20
    for clause in clauses:
        if y < 60:
            c.showPage()
            y = height - 40
        c.drawString(40, y, f"- {clause[:90]}")
        y -= 15

    c.save()
