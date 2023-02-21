
import argparse
from PyPDF2 import PdfFileMerger, PdfWriter, PdfReader

OPERATIONS = {
    "m": "merge",
    "e": "extract",
    "d": "delete"
}
SELECTION = {
    "rg": "range",
    "pg": "page"
}


class PdfEditor:
    args = list()
    print(args)

    def __init__(self):
        argParser = argparse.ArgumentParser(
            exit_on_error=True, description="Welcome to the PDF editor, let's choose an operation")
        subParser = argParser.add_subparsers(dest='command')

        argParser.add_argument(
            "-p", "--pdf",
            nargs='*',
            help="The pdfName you want to select, you only can select multiple for merge operation"
        )
        argParser.add_argument(
            "-o", "--operation",
            choices=OPERATIONS.keys(),
            nargs=1,
            type=str,
            help="The operation you want to execute : merge severals pdf, delete page, extract page", default='merge'
        )
        argParser.add_argument(
            "-pg", "--page",
            nargs='*',
            type=int,
            help="The page numero you want to select, you can select as many you want"
        )
        argParser.add_argument(
            "-rg", "--range",
            nargs=2,
            type=int,
            help="The range of page you want to select [min:max]"
        )
        PdfEditor.args = argParser.parse_args()

    def nbpagespdf(fichierpdf):
        """retourne le nombre de pages du fichier pdf"""
        with open(fichierpdf, "rb") as f:
            return pyPdf.PdfFileReader(f).getNumPages()

    def merge_pdf(self):
        merger = PdfFileMerger()
        mergedPdf = list(PdfEditor.args.pdf)
        for pdf in mergedPdf:
            if pdf.endswith('pdf'):
                merger.append(pdf)
        merger.write('merged_file.pdf')
        merger.close()

    def delete_page_pdf(self):
        # correction du numero de la page a effacer
        PdfEditor.args.page[:] = [p - 1 for p in PdfEditor.args.page]
        for page in range(len(inFile.pages)):
            if page not in PdfEditor.args.page:
                pageToKeep = inFile._get_page(page)
                outFile.add_page(pageToKeep)

    def delete_range_pdf(self):
        # correction de la range de page a effacer
        PdfEditor.args.range[0] = PdfEditor.args.range[0] - 1
        for page in range(len(inFile.pages)):
            if page not in range(PdfEditor.args.range[0], PdfEditor.args.range[1]):
                pageToKeep = inFile._get_page(page)
                outFile.add_page(pageToKeep)

    def extract_page_pdf(self):
        # correction du numero de la page a effacer
        PdfEditor.args.page[:] = [p - 1 for p in PdfEditor.args.page]
        for i, page in zip(range(len(inFile.pages)), range(len(inFile.pages))):
            if page in PdfEditor.args.page:  # cette condition plante
                outFile = PdfWriter()
                pageToExtract = inFile._get_page(page)
                outFile.add_page(pageToExtract)
                try:
                    with open("after_extracted_page_"+str(i+1)+"_"+PdfEditor.args.pdf[0], 'wb') as f:
                        outFile.write(f)
                        print(f)
                except IOError:
                    print(f"Could not read file : {f}")

    def extract_range_pdf(self):
        # correction de la range de page a effacer
        PdfEditor.args.range[0] = PdfEditor.args.range[0] - 1
        for page in range(len(inFile.pages)):
            if page in range(PdfEditor.args.range[0], PdfEditor.args.range[1]):
                pageToKeep = inFile._get_page(page)
                outFile.add_page(pageToKeep)
        try:
            with open("after_extracted_page_"+str(PdfEditor.args.range[0]+1)+"_to_"+str(PdfEditor.args.range[1])+"_"+PdfEditor.args.pdf[0], 'wb') as f:
                outFile.write(f)
        except IOError:
            print(f"Could not read file : {f}")


pdfEdit = PdfEditor()

print("args=%s" % pdfEdit.args)
match pdfEdit.args.operation:
    case ['m'] | ['merge']:
        if pdfEdit.args.pdf:
            pdfEdit.merge_pdf()

    case ['d'] | ['delete']:
        inFile = PdfReader(pdfEdit.args.pdf[0], 'rb')
        outFile = PdfWriter()
        if pdfEdit.args.page:
            pdfEdit.delete_page_pdf()
        elif pdfEdit.args.range:
            pdfEdit.delete_range_pdf()
        try:
            with open("after_deleted_"+pdfEdit.args.pdf[0], 'wb') as f:
                outFile.write(f)
        except IOError:
            print(f"Could not read file : {f}")

    case ['e'] | ['extract']:
        inFile = PdfReader(pdfEdit.args.pdf[0], 'rb')
        outFile = PdfWriter()
        if pdfEdit.args.page:
            pdfEdit.extract_page_pdf()
        elif pdfEdit.args.range:
            pdfEdit.extract_range_pdf()
