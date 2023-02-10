
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


def merge_pdf(args: list):
    merger = PdfFileMerger()
    mergedPdf = list(args.pdf)
    for pdf in mergedPdf:
        if pdf.endswith('pdf'):
            merger.append(pdf)
    merger.write('merged_file.pdf')
    merger.close()


def delete_page_pdf(args: list):
    # correction du numero de la page a effacer
    args.page[:] = [p - 1 for p in args.page]
    for page in range(len(inFile.pages)):
        if page not in args.page:
            pageToKeep = inFile._get_page(page)
            outFile.add_page(pageToKeep)


def delete_range_pdf(args: list):
    # correction de la range de page a effacer
    args.range[0] = args.range[0] - 1
    for page in range(len(inFile.pages)):
        if page not in range(args.range[0], args.range[1]):
            pageToKeep = inFile._get_page(page)
            outFile.add_page(pageToKeep)


def extract_page_pdf(args: list):
    # correction du numero de la page a effacer
    args.page[:] = [p - 1 for p in args.page]
    for i, page in zip(range(len(inFile.pages)), range(len(inFile.pages))):
        if page in args.page:  # cette condition plante
            outFile = PdfWriter()
            pageToExtract = inFile._get_page(page)
            outFile.add_page(pageToExtract)
            with open("after_extracted_page_"+str(i+1)+"_"+args.pdf[0], 'wb') as f:
                outFile.write(f)


def extract_range_pdf(args: list):
    # correction de la range de page a effacer
    args.range[0] = args.range[0] - 1
    for page in range(len(inFile.pages)):
        if page in range(args.range[0], args.range[1]):
            pageToKeep = inFile._get_page(page)
            outFile.add_page(pageToKeep)
    with open("after_extracted_page_"+str(args.range[0]+1)+"_to_"+str(args.range[1])+"_"+args.pdf[0], 'wb') as f:
        outFile.write(f)


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

args = argParser.parse_args()
print("args=%s" % args)
match args.operation:
    case ['m'] | ['merge']:
        if args.pdf:
            merge_pdf(args)

    case ['d'] | ['delete']:
        inFile = PdfReader(args.pdf[0], 'rb')
        outFile = PdfWriter()
        if args.page:
            delete_page_pdf(args)
        elif args.range:
            delete_range_pdf(args)
        with open("after_deleted_"+args.pdf[0], 'wb') as f:
            outFile.write(f)

    case ['e'] | ['extract']:
        inFile = PdfReader(args.pdf[0], 'rb')
        outFile = PdfWriter()
        if args.page:
            extract_page_pdf(args)
        elif args.range:
            extract_range_pdf(args)
