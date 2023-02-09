
import argparse
from PyPDF2 import PdfFileMerger, PdfWriter,PdfReader

argParser = argparse.ArgumentParser(exit_on_error=True)
argParser.usage = 'Use it like this.'
argParser.add_argument("-p", "--pdf", nargs='*',
                       help="The pdfName you want to select")
argParser.add_argument("-o", "--operation", nargs='*',
                       help="The operation you want to execute : merge severals pdf, delete page", default='merge')
argParser.add_argument("-pg","--page",nargs='*',type = int, help="The page numero you want to delete")
argParser.add_argument("-rg","--range",nargs='*',type = int, help="The range of page you want to delete")
args = argParser.parse_args()
print("args=%s" % args)
match args.operation:
    case ['merge']:
        if args.pdf:
            merger = PdfFileMerger()
            mergedPdf = list(args.pdf)
            for pdf in mergedPdf:
                if pdf.endswith('pdf'):
                    merger.append(pdf)
            merger.write('merged_file.pdf')
            merger.close()
    
    case ['delete']:
        if args.page:
            args.page[:] = [p - 1 for p in args.page] # correction du numero de la page a effacer
            inFile = PdfReader(args.pdf[0],'rb')
            outFile = PdfWriter()
            
            for page in range(len(inFile.pages)):
                if page not in args.page:
                    pageToKeep = inFile._get_page(page)
                    outFile.add_page(pageToKeep)
            with open("new_"+args.pdf[0] , 'wb') as f:
                outFile.write(f)
                
    case ['extract']:

        
