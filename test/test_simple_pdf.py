import unittest
import super_simple_pdf


class TestSimplePdf(unittest.TestCase):

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

    def test_words(self):
        pdf = super_simple_pdf.SimplePdf("test1.pdf")
        pdf.add_text("First")
        pdf.add_text("Second")
        pdf.add_text("Bye!")
        pdf.save()

    def test_normal_text(self):
        pdf = super_simple_pdf.SimplePdf("test2.pdf")

        pdf.add_text(self.text)
        pdf.save()

    def test_long_text(self):
        pdf = super_simple_pdf.SimplePdf("test3.pdf")

        pdf.add_text(self.text)
        pdf.add_text(self.text)
        pdf.add_text(self.text)
        pdf.save()

    def test_long_text_with_headers(self):
        pdf = super_simple_pdf.SimplePdf("test4.pdf")

        pdf.add_header(self.long_header)
        pdf.add_text(self.text)
        pdf.add_header(self.short_header)
        pdf.add_text(self.text)
        pdf.add_header(self.short_header)
        pdf.add_text(self.text)
        pdf.save()

if __name__ == '__main__':
    unittest.main()