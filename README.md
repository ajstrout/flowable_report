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
