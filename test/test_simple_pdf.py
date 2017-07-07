import unittest
from super_simple_pdf import SimplePdf


class TestSimplePdf(unittest.TestCase):

    short_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor " \
           "incididunt ut labore et dolore magna aliqua. Viverra suspendisse potenti nullam " \
           "ac. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh. " \
           "Porttitor rhoncus dolor purus non enim praesent elementum facilisis. Vitae " \
           "tortor condimentum lacinia quis."

    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor " \
           "incididunt ut labore et dolore magna aliqua. Viverra suspendisse potenti nullam " \
           "ac. Aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh. " \
           "Porttitor rhoncus dolor purus non enim praesent elementum facilisis. Vitae " \
           "tortor condimentum lacinia quis. Scelerisque varius morbi enim nunc faucibus a " \
           "pellentesque sit. Felis eget velit aliquet sagittis id consectetur. Luctus " \
           "venenatis lectus magna fringilla urna porttitor rhoncus. Nec ultrices dui sapien " \
           "eget mi proin sed libero enim. Malesuada bibendum arcu vitae elementum curabitur " \
           "vitae. Non odio euismod lacinia at quis risus sed vulputate. Nam libero justo " \
           "laoreet sit amet cursus sit amet dictum. Commodo quis imperdiet massa tincidunt " \
           "nunc pulvinar sapien. Enim facilisis gravida neque convallis a cras semper. " \
           "Accumsan tortor posuere ac ut consequat semper viverra. Et malesuada fames ac " \
           "turpis egestas maecenas pharetra. Ornare arcu dui vivamus arcu. Ut porttitor leo " \
           "a diam sollicitudin tempor id eu. Lectus nulla at volutpat diam ut venenatis. " \
           "Malesuada pellentesque elit eget gravida cum sociis.\n\nCongue mauris rhoncus " \
           "aenean vel elit scelerisque. Tortor vitae purus faucibus ornare. Id interdum " \
           "velit laoreet id donec. Porta lorem mollis aliquam ut porttitor leo a diam. Ut " \
           "faucibus pulvinar elementum integer enim. Vitae nunc sed velit dignissim sodales " \
           "ut. Neque gravida in fermentum et sollicitudin. Tincidunt lobortis feugiat " \
           "vivamus at augue eget arcu dictum varius. Consectetur adipiscing elit duis " \
           "tristique sollicitudin. A lacus vestibulum sed arcu non odio. Et odio " \
           "pellentesque diam volutpat commodo sed. Vitae proin sagittis nisl rhoncus mattis " \
           "rhoncus. Phasellus vestibulum lorem sed risus. Purus sit amet luctus venenatis " \
           "lectus magna fringilla urna porttitor.\n\nSuspendisse potenti nullam ac tortor. " \
           "Non pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus. " \
           "Euismod nisi porta lorem mollis aliquam ut. A condimentum vitae sapien " \
           "pellentesque habitant morbi tristique senectus. Convallis a cras semper auctor " \
           "neque vitae. Ut lectus arcu bibendum at varius. Neque sodales ut etiam sit amet. " \
           "Quis varius quam quisque id diam vel quam. Nunc scelerisque viverra mauris in " \
           "aliquam sem fringilla. Felis imperdiet proin fermentum leo vel orci porta non. " \
           "Rhoncus est pellentesque elit ullamcorper dignissim cras. Leo in vitae turpis " \
           "massa sed elementum. Tellus pellentesque eu tincidunt tortor aliquam nulla. Sed " \
           "augue lacus viverra vitae congue eu consequat ac. Ac feugiat sed lectus " \
           "vestibulum. Arcu felis bibendum ut tristique et egestas quis ipsum. Elementum " \
           "sagittis vitae et leo duis ut diam. Semper auctor neque vitae tempus quam " \
           "pellentesque nec.\n\nPhasellus vestibulum lorem sed risus ultricies tristique " \
           "nulla aliquet enim. Pulvinar sapien et ligula ullamcorper. Diam maecenas " \
           "ultricies mi eget mauris pharetra et ultrices neque. Lacus luctus accumsan " \
           "tortor posuere ac ut consequat semper viverra. Fringilla urna porttitor rhoncus " \
           "dolor purus non enim praesent elementum. Est ante in nibh mauris cursus. Viverra " \
           "ipsum nunc aliquet bibendum enim facilisis gravida neque. Dignissim suspendisse " \
           "in est ante. Eget velit aliquet sagittis id consectetur purus ut faucibus " \
           "pulvinar. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget " \
           "egestas. Integer eget aliquet nibh praesent tristique."

    long_header = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor " \
        "incididunt ut labore et dolore magna aliqua."

    short_header = "Integer eget aliquet"

    large_image_filename = "resources/amsterdam_large_by_kris_roksela.jpg"
    small_image_filename = "resources/amsterdam_small_by_kris_roksela.jpg"

    def test_no_content(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.save()

    def test_words(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text("First")
        pdf.add_text("Second")
        pdf.add_text("Bye!")
        pdf.save()

    def test_normal_text(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.text)
        pdf.save()

    def test_long_text(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.text)
        pdf.add_text(self.text)
        pdf.add_text(self.text)
        pdf.save()

    def test_long_text_with_headers(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_header(self.long_header)
        pdf.add_text(self.text)
        pdf.add_header(self.short_header)
        pdf.add_text(self.text)
        pdf.add_header(self.short_header)
        pdf.add_text(self.text)
        pdf.save()

    def test_image(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text("First")
        pdf.add_image(self.small_image_filename)
        pdf.save()

    def test_text_with_image(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_header(self.short_header)
        pdf.add_header(self.short_header)
        pdf.add_header(self.short_header)
        pdf.add_text(self.text)
        pdf.add_image(self.small_image_filename)
        pdf.add_text("End line")
        pdf.save()

    def test_large_image(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.short_text)
        pdf.add_image(self.large_image_filename)
        pdf.add_text(self.short_text)
        pdf.save()

    def test_table(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.short_text)
        data = [["First Name", "Last Name", "Email"],
                ["John", "Red", "j.red@example.org"],
                ["Sarah", "Leitz", "s.leitz@example.org"],
                ["Tom", "Porter", "t.porter@example.org"],
                ["Christie", "Owl", "c.owl@example.org"]]
        pdf.add_table(data)
        pdf.add_text(self.short_text)
        pdf.save()

    def test_table_many_columns(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.short_text)
        data = [["First Name", "Last Name", "Email",
                 "First Name", "Last Name", "Email", "First Name", "Last Name", "Email"],
                ["John", "Red", "j.red example.org",
                 "John", "Red", "j.red example.org", "John", "Red", "j.red example.org"],
                ["Sarah", "Leitz", "s.leitz example.org",
                 "Sarah", "Leitz", "s.leitz example.org", "Sarah", "Leitz", "s.leitz example.org"],
                ["Tom", "Porter", "t.porter example.org",
                 "Tom", "Porter", "t.porter example.org", "Tom", "Porter", "t.porter example.org"],
                ["Christie", "Owl", "c.owl example.org",
                 "Christie", "Owl", "c.owl example.org", "Christie", "Owl", "c.owl example.org"]]
        pdf.add_table(data)
        pdf.add_text(self.short_text)
        pdf.save()

    def test_large_table(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.short_text)
        data = [["First Name", "Last Name", "Email"],
                [self.short_text, self.short_text, "j.red@example.org"],
                [self.short_text, self.short_text, "s.leitz@example.org"],
                [self.short_text, self.short_text, "t.porter@example.org"],
                [self.short_text, self.short_text, "c.owl@example.org"]]
        pdf.add_table(data)
        pdf.add_text(self.short_text)
        pdf.save()

    def test_filename_later(self):
        pdf = SimplePdf()

        pdf.add_text("First")
        pdf.add_text("Second")
        pdf.add_text("Bye!")
        pdf.filename = self._testMethodName + ".pdf"
        pdf.save()

    def test_filename_save_twice(self):
        pdf = SimplePdf()

        pdf.add_text("First")
        pdf.add_text("Second")
        pdf.add_text("Bye!")
        pdf.filename = self._testMethodName + "_1.pdf"
        pdf.save()

        print(pdf.parts)
        pdf.filename = self._testMethodName + "_2.pdf"
        pdf.save()

    def test_no_filename(self):
        pdf = SimplePdf()

        pdf.add_text("First")
        pdf.add_text("Second")
        pdf.add_text("Bye!")

        with self.assertRaises(TypeError):
            pdf.save()

    def test_custom_page_size(self):
        pdf = SimplePdf(self._testMethodName + ".pdf", (500, 500))

        pdf.add_text("First")
        pdf.add_text("Second")
        pdf.add_text("Bye!")
        pdf.save()

    def test_table_one_row(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.short_text)
        data = [["First Name", "Last Name", "Email"]]
        pdf.add_table(data)
        pdf.add_text(self.short_text)
        pdf.save()

    def test_table_irregular(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.short_text)
        data = [["First Name", "Last Name", "Email", "Address"],
                ["John", "Red"],
                ["Sarah", "Leitz", "s.leitz@example.org"],
                ["Tom", "Porter"],
                ["Christie", "Owl", "c.owl@example.org"]]
        pdf.add_table(data)
        pdf.add_text(self.short_text)
        pdf.save()

    def test_table_irregular_2(self):
        pdf = SimplePdf(self._testMethodName + ".pdf")

        pdf.add_text(self.short_text)
        data = [["First Name", "Last Name"],
                ["Sarah", "Leitz", "s.leitz@example.org", "Buffalo, NY"],
                ["Tom", "Porter"],
                ["Christie", "Owl", "c.owl@example.org"]]
        pdf.add_table(data)
        pdf.add_text(self.short_text)
        pdf.save()

    # TODO: run actual test assertions in each test

if __name__ == '__main__':
    unittest.main()
