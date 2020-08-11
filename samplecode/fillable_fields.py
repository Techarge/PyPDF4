"""
Sample code that copies a PDF, changing field values along the way (i.e. using
a PDF with fillable fields as a template).

FYI: The fillable_form.pdf used in this demo was created via LibreOffice.
"""
import sys
from pypdf import PdfFileWriter, PdfFileReader

root_folder = "samplecode/"
template_name = "fillable_form.pdf"

def discover_fields(template_pdf):
    available_fields = template_pdf.getFields()
    if available_fields:
        print("Available fields:")
        for fieldname in available_fields:
            print("    %s" % fieldname)
    else:
        print("ERROR: '" + template_name + "' has no text fields.")
        sys.exit(1)

def fill_in_pdf(template_pdf, field_values, filename):
    output = PdfFileWriter(filename)
    output.have_viewer_render_fields()
    for page_no in range(template_pdf.numPages):
        template_page = template_pdf.getPage(page_no)
        output.addPage(template_page)
        page = output.getPage(page_no)
        output.updatePageFormFieldValues(page, field_values, read_only=True)
    output.write()
    print("Created '%s'" % (filename))


def main():
    template_pdf = PdfFileReader(open(root_folder + template_name, "rb"),
        strict=False)

    employee_john = {
        "employee_name": "John Hardworker",
        "employee_id": "0123",
        "department": "Human Resources",
        "manager_name": "Doris Stickler",
        "manager_id": "0072"
    }
    employee_cyndi = {
        "employee_name": "Cyndi Smartworker",
        "employee_id": "0199",
        "department": "Engineering",
        "manager_name": "Ida Wright",
        "manager_id": "0051"
    }

    discover_fields(template_pdf)
    fill_in_pdf(template_pdf, employee_john, root_folder +
        "JohnHardworder.pdf")
    fill_in_pdf(template_pdf, employee_cyndi, root_folder +
        "CyndiSmartworker.pdf")

if __name__ == "__main__":
    main()
