import os
import argparse
from PyPDF2 import PdfFileMerger

argParser = argparse.ArgumentParser(exit_on_error=True)
argParser.add_argument("-p", "--pdf",nargs='*', help="input the pdfName you want to merge")
args = argParser.parse_args()
print("args=%s" % args)
print("args.pdf=%s" % args.pdf)
merger = PdfFileMerger()


pdfs = list(args.pdf)
for pdf in pdfs:
    if pdf.endswith('pdf'):
        merger.append(pdf)
merger.write('merged_file.pdf')
merger.close() 