from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from datetime import datetime
import html


def save_pdf_report(password, result):
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal_style = styles["Normal"]

    # Экранируем HTML-символы
    safe_password = html.escape(password)

    elements.append(Paragraph("PASSWORD SECURITY REPORT", title_style))
    elements.append(Spacer(1, 0.3 * inch))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(f"<b>Password:</b> {safe_password}", normal_style))
    elements.append(Paragraph(f"<b>Generated at:</b> {datetime.now()}", normal_style))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    elements.append(Spacer(1, 0.3 * inch))

    for key, value in result.items():
        safe_value = html.escape(str(value))
        elements.append(Paragraph(f"<b>{key}:</b> {safe_value}", normal_style))
        elements.append(Spacer(1, 0.15 * inch))

    doc.build(elements)
    return filename