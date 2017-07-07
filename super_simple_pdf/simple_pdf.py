from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


class SimplePdf(object):
    """
    SimplePdf helps to put your content into a PDF document without hassle.

    No styles, no fonts, just standard black text, black borders and scaled images.
    """

    _default_page_size = letter
    _default_spacer_height = 10
    _default_spacer_width = 1
    _default_margin = 72
    _default_font_size = 10
    _default_header_font_size = 20
    _default_leading_ratio = 1.5

    def __init__(self, filename=None, page_size=_default_page_size):
        """
        Constructs document with given filename and page size.

        Default page size is US Letter.
        File won't be saved on disk until you explicitly call save().

        :param filename: The file path where PDF will be saved.
        :param page_size: Page size as tuple(width, height)
        """
        self.filename = filename
        self.parts = []
        self._page_size = page_size
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
        """
        Adds text to the document.

        Text is automatically wrapped.

        :param text: Any text as string
        """
        content = SimplePdf._prepare_text_for_reportlab(text)

        self.parts.append(Paragraph(content, self.styles["SimpleStyle"]))
        self._add_some_space()

    def add_header(self, header):
        """
        Adds header to the document.

        Text is automatically wrapped.

        :param header: Any text as string
        """
        content = SimplePdf._prepare_text_for_reportlab(header)

        self._add_some_space()
        self.parts.append(Paragraph(content, self.styles["SimpleHeaderStyle"]))
        self._add_some_space()

    def add_image(self, filename):
        """
        Adds image to the document.

        Images are scaled automatically to fit within margins.

        :param filename: File path of an image
        """
        original_image = Image(filename)
        aspect_ratio = original_image.imageHeight / float(original_image.imageWidth)

        max_width = self._page_size[0] - (2 * self.margin)
        width = min(original_image.imageWidth, max_width)
        image = Image(filename, width=width, height=(width * aspect_ratio))

        self.parts.append(image)
        self._add_some_space()

    def add_table(self, data):
        """
        Adds table to the document.

        :param data: List of lists to put in the table
        """
        matrix = [[self._wrap_text(cell) for cell in row] for row in data]
        table = Table(matrix)

        # set all borders black
        table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
                               ('BOX', (0, 0), (-1, -1), 1, colors.black)]))

        self.parts.append(table)
        self._add_some_space()

    def save(self):
        """
        Saves PDF file on disk.

        NOTE: Please make sure filename is set before saving.
        """
        if self.filename is None:
            raise TypeError("filename not set")
        if not self.parts:
            # avoid saving documents with no parts
            # PDF viewers can't open such documents
            self._add_some_space()

        doc = SimpleDocTemplate(self.filename, pagesize=self._page_size,
                                rightMargin=self.margin, leftMargin=self.margin,
                                topMargin=self.margin, bottomMargin=self.margin)

        doc.build(self.parts)

    def _add_some_space(self):
        """
        Adds some blank space after last part.
        """
        self.parts.append(Spacer(self.spacer_width, self.spacer_height))

    def _wrap_text(self, text):
        """
        Wraps the text by converting it to Paragraph.

        Text in Paragraphs is wrapped automatically.

        :param text: string to wrap
        :return: wrapped text as Paragraph
        """
        paragraph = Paragraph(text, self.styles["SimpleStyle"])
        return paragraph

    @staticmethod
    def _prepare_text_for_reportlab(text):
        """
        Transforms text for processing by reportlab.

        End of lines are replaced by HTML tags to preserve end of line.
        :param text: string to transform
        :return: transformed string
        """
        content = str(text).replace('\n', '<br />\n')
        return content

    # TODO: add support for converting PDF to text
