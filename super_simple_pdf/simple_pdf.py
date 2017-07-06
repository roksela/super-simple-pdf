from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class SimplePdf(object):

    _default_page_size = letter
    _default_spacer_height = 10
    _default_spacer_width = 1
    _default_margin = 72

    def __init__(self, filename, page_size=_default_page_size):
        self.filename = filename
        self.parts = []
        self.page_size = page_size
        self.spacer_height = SimplePdf._default_spacer_height
        self.spacer_width = SimplePdf._default_spacer_width
        self.margin = SimplePdf._default_margin

        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='SimpleStyle', fontSize=10, leading=15))
        self.styles.add(ParagraphStyle(name='SimpleHeaderStyle', fontSize=20, leading=30))

    @staticmethod
    def _prepare_text_for_reportlab(text):
        # reportlab needs html tag to preserve end of line
        content = str(text).replace('\n', '<br />\n')
        return content

    def add_text(self, text):
        content = SimplePdf._prepare_text_for_reportlab(text)

        self.parts.append(Paragraph(content, self.styles["SimpleStyle"]))
        self.parts.append(Spacer(self.spacer_width, self.spacer_height))

    def add_header(self, header):
        content = SimplePdf._prepare_text_for_reportlab(header)

        self.parts.append(Spacer(self.spacer_width, self.spacer_height))
        self.parts.append(Paragraph(content, self.styles["SimpleHeaderStyle"]))
        self.parts.append(Spacer(self.spacer_width, self.spacer_height))

    def add_image(self, filename):
        original_image = Image(filename)
        aspect_ratio = original_image.imageHeight / float(original_image.imageWidth)

        max_width = self.page_size[0] - (2 * self.margin)
        width = min(original_image.imageWidth, max_width)
        image = Image(filename, width=width, height=(width * aspect_ratio))

        self.parts.append(image)
        self.parts.append(Spacer(self.spacer_width, self.spacer_height))

    def save(self):
        doc = SimpleDocTemplate(self.filename, pagesize=self.page_size,
                                rightMargin=self.margin, leftMargin=self.margin,
                                topMargin=self.margin, bottomMargin=self.margin)

        doc.build(self.parts)