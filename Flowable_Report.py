"""
This module is for generating flowable "basic" reports using Reportlab with
the main focus to quickly generate a report.

The intent is a simplier way to create .pdf reports based on the ReportLab
module. A story which is a list object is initialized when the Report object
is created. The "story" is populated by using the Report functions print_*.

Module is made of the below functions that will assist in generating a report
1. Report.first_page is basic set-up of a "Cover Page"
1.1 Report.set_Title is a helper function to get around a ReportLab quirk
1.2 Report.set_SecondaryTitle a helper function to get around a ReportLab quirk
2. Report.secondary_page is set-up of the remaining pages
3. Report.print_spacer is the generic line break
4. Report.print_line will print a single or multi line string
5. Report.print_list will print each row of a list of list
6. Report.print_image will print an image object
7. Report.generate will create the report
"""
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

# Global variables
styles = getSampleStyleSheet()


class Report():
    """ Class definition of a report """
    def __init__(self, filename, title, secondary_title):
        self.filename = filename
        self.story = []
        self.doc = SimpleDocTemplate(filename)
        self.canvas = Canvas(filename)
        self.global_title = Report.set_title(title)
        self.global_sectitle = Report.set_secondarytitle(secondary_title)

    @classmethod
    def set_title(self, title):
        """
        Purpose:
            This allows the user to put a title into the report.
        Arguments:
            title: string
        Return Value: None
            Creates a global variable to populate the title
        """
        global global_title
        global_title = title

    @classmethod
    def set_secondarytitle(self, secondary_title):
        """
        Purpose:
            This allows the user to put a secondary title into the
            report.
        Arguments:
            secondary_title: string
        Return Value: None
            Creates a global variable to populate the secondary title
        """
        global global_sectitle
        global_sectitle = secondary_title

    @classmethod
    def first_page(self, canvas, doc):
        """
        Purpose:
            The set-up information to draw the "cover page", this
            function does not need to be called
        Arguments:
            canvas: list
                the list object that contains the parts of the report
            doc: string
                path to the document object unused at the moment but here
                in case the first page of the document needs to be edited
        Return Value: None
            sets up the template for the cover page
        """

        canvas.saveState()
        canvas.setFont('Times-Bold', 18)
        canvas.drawCentredString(8.5 * inch / 2, 11.2 * inch,
                                 global_title)
        canvas.setFont('Times-Bold', 16)
        canvas.drawCentredString(8.5 * inch / 2, 10.8 * inch,
                                 global_sectitle)
        canvas.setFont('Times-Roman', 9)
        canvas.drawString(inch, 0.75 * inch, "Page 1")
        canvas.restoreState()

    @classmethod
    def secondary_page(self, canvas, doc):
        """
        Purpose:
            The set-up information to draw the page template, this function
            does not need to be called
        Arguments:
            canvas: list
                the list object that contains the parts of the report
            doc: string
                path to the document object
        Return Value: None
            sets up the template for the secondary pages
        """

        canvas.saveState()
        canvas.setFont('Times-Bold', 8)
        canvas.drawString(inch, 0.75 * inch, "Page {0}".format(doc.page))
        canvas.restoreState()

    def print_spacer(self):
        """
        Purpose:
            This is the standard spacer for the report - it is made of two
            vertical whitespaces and one line of dashes
        Arguments:
            None: self
        Return Value: None
            Appends a line spacer into the "story"
        """

        self.story.append(Spacer(1, 0.1 * inch))
        l_style = styles["Normal"]
        l = Paragraph('-----------------------------------------------------' +
                      '-----------------------------------------------------' +
                      '----------------',
                      l_style)
        self.story.append(l)
        self.story.append(Spacer(1, 0.1 * inch))

    def print_line(self, input_line):
        """
        Purpose:
            Takes a string of text and prints that paragraph to the report
        Arguments:
            input_list: string
                full name of the report
        Return Value: None
            Appends a string into the "story"
        """

        l_style = styles["Normal"]
        p = Paragraph(input_line, l_style)
        self.story.append(p)

    def print_list(self, input_list):
        """
        Purpose:
            Takes a list that contains lists and prints it out to the report
            one row at a time
        Arguments:
            input_list: list
                A list too be appended to the report
        Return Value: None
            Appends a list into the "story"
        """

        try:
            l_style = styles["Normal"]
            for line in input_list:
                line_row = line[0]
                p = Paragraph(line_row, l_style)
                self.story.append(p)
        except TypeError:
            self.print_line("Object needs to be of type list")

    def print_image(self, input_image, width, height):
        """
        Purpose:
            Pushes an imgage into the story so it can be printed in the report
        Arguments:
            input_image: string
                full name of the image file
            X: int
                Determines the scale of image in the horizontal
            Y: int
                Determines the scale of image in the vertical
        Return Value: None
            Appends an image into the "story" list to be printed later
        """
        try:
            img = Image(input_image)
            if width * inch > 8 and height * inch > 9:
                img._restrictSize(7 * inch, 8 * inch)
                self.story.append(img)
            elif width * inch > 8 and height * inch < 9:
                img._restrictSize(7 * inch, height * inch)
                self.story.append(img)
            elif width * inch < 8 and height * inch > 9:
                img._restrictSize(width * inch, 8 * inch)
                self.story.append(img)
            else:
                img._restrictSize(width * inch, height * inch)
                self.story.append(img)
        except ValueError:
            self.print_line("The image did not print")

    def generate(self):
        """
        Purpose:
            Function to generate the report
        Arguments:
            self: None
        Return Value: None
            Creates the .pdf report
        """

        self.doc.build(self.story,
                       onFirstPage=self.first_page,
                       onLaterPages=self.secondary_page)
