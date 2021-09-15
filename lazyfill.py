import pdfrw
pdfrw.__version__

initial_pdf = "Generic.pdf"
output_pdf = "filled.pdf"
template_pdf = pdfrw.PdfReader(initial_pdf)

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

##keys taken from akdux.com

columns = []

for page in template_pdf.pages:
    annotations = page[ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                columns.append(key)

# print(columns)
print(len(columns))
