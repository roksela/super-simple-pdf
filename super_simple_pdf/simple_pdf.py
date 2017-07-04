from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class SimplePdf(object):

    def __init__(self, filename):
        self.filename = filename
        self.parts = []

        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='SimpleStyle', fontSize=12, leading=18))

    def addText(self, text):
        content = str(text).replace('\n', '<br />\n')
        self.parts.append(Paragraph(content, self.styles["SimpleStyle"]))
        self.parts.append(Spacer(1, 12))

    def save(self):
        doc = SimpleDocTemplate(self.filename, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=72)

        doc.build(self.parts)