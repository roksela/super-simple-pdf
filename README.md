# super-simple-pdf
Super simple PDF generation in Python.
This library helps to create simple documents based on your content.

We support headers, text, images and tables. No fancy colors or fonts.

Perfect solution if you just need to put your content into a PDF.

This project uses ReportLab open-source PDF Toolkit.

## Getting Started

```python
from super_simple_pdf import SimplePdf

pdf = SimplePdf("test1.pdf")

pdf.add_header("Header")
pdf.add_text("Text A")
pdf.add_text("Text B")
pdf.add_image("image1.jpg")
pdf.add_text("Text C")
pdf.add_image("image2.jpg")

pdf.save()

```

## Tables

```python
from super_simple_pdf import SimplePdf

pdf = SimplePdf("test2.pdf")

pdf.add_text("Text")
data = [("First Name", "Last Name", "Email"),
        ("John", "Red", "j.red@example.org"),
        ("Sarah", "Leitz", "s.leitz@example.org"),
        ("Tom", "Porter", "t.porter@example.org"),
        ("Christie", "Owl", "c.owl@example.org")]
pdf.add_table(data)

pdf.save()

```

## Author

Kris Roksela kris@dataservices.pro