
import argparse
from PyPDF2 import PdfFileMerger, PdfWriter,PdfReader

argParser = argparse.ArgumentParser(exit_on_error=True)
argParser.usage = 'Use it like this.'
argParser.add_argument("-p", "--pdf", nargs='*',
                       help="The pdfName you want to select")
argParser.add_argument("-o", "--operation", nargs='*',
                       help="The operation you want to execute : merge severals pdf, delete page", default='merge')
argParser.add_argument("-pg","--page",nargs='*',type = int, help="The page numero you want to select, you can select as many you want")
argParser.add_argument("-rg","--range",nargs=2,type = int, help="The range of page you want to select [min:max]")
args = argParser.parse_args()
print("args=%s" % args)
print(args.range)

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

        inFile = PdfReader(args.pdf[0],'rb')
        outFile = PdfWriter()

        if args.page :
            args.page[:] = [p - 1 for p in args.page] # correction du numero de la page a effacer
            for page in range(len(inFile.pages)):

                if page not in args.page:
                    pageToKeep = inFile._get_page(page)
                    outFile.add_page(pageToKeep)

        elif args.range:
            args.range[0] = args.range[0] - 1  # correction de la range de page a effacer
            for page in range(len(inFile.pages)):
                if page not in range(args.range[0],args.range[1]): 
                    print(args.range[0],args.range[1])
                    pageToKeep = inFile._get_page(page)
                    outFile.add_page(pageToKeep)

        with open("after_deleted_"+args.pdf[0] , 'wb') as f:
            outFile.write(f)
                
    case ['extract']:
        inFile = PdfReader(args.pdf[0],'rb')
        if args.page:
            args.page[:] = [p - 1 for p in args.page] # correction du numero de la page a effacer
            for i, page in zip(range(len(inFile.pages)),range(len(inFile.pages))):
                if page in args.page: #cette condition plante
                    print("coucou")
                    outFile = PdfWriter()
                    pageToExtract = inFile._get_page(page)
                    outFile.add_page(pageToExtract)
                    with open("after_extracted_Page_"+str(i)+"_"+args.pdf[0] , 'wb') as f:
                        outFile.write(f)
