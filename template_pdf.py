from reportlab.pdfgen import canvas

def create_blank_pdf(filename):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "USE TEMPLATE_PDF.PY TO MAKE A TEMPLATE LIKE THIS")
    c.save()

create_blank_pdf("template.pdf")
