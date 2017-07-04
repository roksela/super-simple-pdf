from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class SimplePdf(object):

    def __init__(self, filename):
        self.filename = filename
        self.parts = []

        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='SimpleStyle', fontSize=10, leading=15))
        self.styles.add(ParagraphStyle(name='SimpleHeaderStyle', fontSize=20, leading=30))

    def add_text(self, text):
        content = str(text).replace('\n', '<br />\n')
        self.parts.append(Paragraph(content, self.styles["SimpleStyle"]))
        self.parts.append(Spacer(1, 10))

    def add_header(self, header):
        self.parts.append(Spacer(1, 10))
        content = str(header).replace('\n', '<br />\n')
        self.parts.append(Paragraph(content, self.styles["SimpleHeaderStyle"]))
        self.parts.append(Spacer(1, 10))

    def save(self):
        doc = SimpleDocTemplate(self.filename, pagesize=letter,
                                rightMargin=72, leftMargin=72,
                                topMargin=72, bottomMargin=72)

        doc.build(self.parts)