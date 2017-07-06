from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class SimplePdf(object):

    _default_page_size = letter
    _default_spacer_height = 10
    _default_spacer_width = 1
    _default_margin = 72
    _default_font_size = 10
    _default_header_font_size = 20
    _default_leading_ratio = 1.5

    def __init__(self, filename, page_size=_default_page_size):
        self.filename = filename
        self.parts = []
        self.page_size = page_size
        self.spacer_height = SimplePdf._default_spacer_height
        self.spacer_width = SimplePdf._default_spacer_width
        self.margin = SimplePdf._default_margin
        self.font_size = SimplePdf._default_font_size
        self.header_font_size = SimplePdf._default_header_font_size
        self.leading_ratio = SimplePdf._default_leading_ratio

        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='SimpleStyle', fontSize=self.font_size,
                                       leading=self.font_size * self.leading_ratio))
        self.styles.add(ParagraphStyle(name='SimpleHeaderStyle', fontSize=self.header_font_size,
                                       leading=self.header_font_size * self.leading_ratio))

    def add_text(self, text):
        content = SimplePdf._prepare_text_for_reportlab(text)

        self.parts.append(Paragraph(content, self.styles["SimpleStyle"]))
        self._add_some_space()

    def add_header(self, header):
        content = SimplePdf._prepare_text_for_reportlab(header)

        self._add_some_space()
        self.parts.append(Paragraph(content, self.styles["SimpleHeaderStyle"]))
        self._add_some_space()

    def add_image(self, filename):
        original_image = Image(filename)
        aspect_ratio = original_image.imageHeight / float(original_image.imageWidth)

        max_width = self.page_size[0] - (2 * self.margin)
        width = min(original_image.imageWidth, max_width)
        image = Image(filename, width=width, height=(width * aspect_ratio))

        self.parts.append(image)
        self._add_some_space()

    def add_table(self, data):

        matrix = [[self._wrap_text(cell) for cell in row] for row in data]
        table = Table(matrix)

        # set all borders black
        table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
                               ('BOX', (0, 0), (-1, -1), 1, colors.black)]))

        self.parts.append(table)
        self._add_some_space()

    def save(self):
        doc = SimpleDocTemplate(self.filename, pagesize=self.page_size,
                                rightMargin=self.margin, leftMargin=self.margin,
                                topMargin=self.margin, bottomMargin=self.margin)

        doc.build(self.parts)

    def _add_some_space(self):
        self.parts.append(Spacer(self.spacer_width, self.spacer_height))

    def _wrap_text(self, text):
        # convert text to Paragraph
        # text in Paragraphs is wrapped automatically
        paragraph = Paragraph(text, self.styles["SimpleStyle"])
        return paragraph

    @staticmethod
    def _prepare_text_for_reportlab(text):
        # reportlab needs html tag to preserve end of line
        content = str(text).replace('\n', '<br />\n')
        return content