# Flowable_Report

This module is a simple wrapper for the ReportLab module.

The purpose is a simplier and quicker way to create .pdf reports based on the ReportLab
module using an object oriented design. 

## Use
A story which is a list object is created when the Report object
is initialized. The "story" is populated by using the Report functions print_*. 
After the story has been populated generate the report using the generate function.

## Module is made of the below functions that will assist in generating a report
1. Report.first_page is basic set-up of a "Cover Page"
2. Report.set_Title is a helper function to get around a ReportLab quirk
3. Report.set_SecondaryTitle a helper function to get around a ReportLab quirk
4. Report.secondary_page is set-up of the remaining pages
5. Report.print_spacer is the generic line break
6. Report.print_line will print a single or multi line string
7. Report.print_list will print each row of a list of list
8. Report.print_image will print an image object
9. Report.generate will create the report

## Dependencies:
* from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
* from reportlab.lib.styles import getSampleStyleSheet
* from reportlab.lib.units import inch
* from reportlab.pdfgen.canvas import Canvas

## Example
```Python
import os
import Flowable_Report
import matplotlib.pyplot as plt


def main():

    # Initialze the report class object
    report = Flowable_Report.Report(
        r'C:\Users\astrout.000\Desktop\Example.pdf',
        "Report Example",
        "An analysis of some data"
    )
    # Add a spacer by calling the class object and using the print_spacer method
    report.print_spacer()
    # Some example data in list format
    data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    data1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # Add a line of text explaining the data using the print_line method
    report.print_line(
        "A list of the data the we have created"
    )
    # Add the data list to the report using the print_list method
    report.print_list(data)
    # Create an image
    plt.plot(data, data1)
    plt.savefig(r"C:\Users\astrout.000\Desktop\foo.jpg", bbox_inches='tight')
    # Add image to the report
    report.print_image(r"C:\Users\astrout.000\Desktop\foo.jpg", 1, 1)
    # Add an additional image to report to see what happens when image is
    # added and forces a page break
    report.print_image(r"C:\Users\astrout.000\Desktop\foo.jpg", 1, 1)
    # Generate the .pdf report
    report.generate()
    os.remove(r"C:\Users\astrout.000\Desktop\foo.jpg")


if __name__ == '__main__':
    main()
```

### Output
![Report](https://github.com/ajstrout/flowable_report/blob/master/Example.pdf)
