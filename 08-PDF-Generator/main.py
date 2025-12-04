from reportlab.pdfgen import canvas

c = canvas.Canvas("invoice.pdf")
c.setFont("Helvetica-Bold", 20)
c.drawString(100, 750, "INVOICE #001")
c.setFont("Helvetica", 12)
c.drawString(100, 700, "Customer: Abdulkadir Turan")
c.drawString(100, 680, "Service: Python Development")
c.drawString(100, 660, "Total: $500.00")
c.save()
print("Invoice Generated: invoice.pdf")