# PDFEditor
**Tool which edits fastly PDF files without a need to convert it back in Word extension
 operation -o or --operation :** 
- *Delete one page or more of PDF, "delete"
- Add one or more pdf one after others, option "merge" 
- Delete one page or more of PDF, option "extract"*

**Mode de selection :**
** Previous operations need to be renseigned of a selection mode :**
- *select one or more page "pg" followed by the number of page you want to, spaced out.
- select a page range "rg" followede by the lower and upper bound page you want to, spaced out.*

**How to use it ? :**
 1) Clone the repo and follow the next exemple
Exemple : 
  I need to : 
  - extract the first pdf page : `python PdfMerger.py -p pdf_name.pdf -o e -pg 1`   
  - delete the 1st, 3rd and 5th page pdf pages : `python PdfMerger.py -p pdf_Name.pdf -o d -pg 1 3 5`
  - extract from the 1st to the 5th page : `python PdfMerger.py -p pdf_name.pdf -o d -rg 1 5`
  - merge 2 pdf in one : `python PdfMerger.py -p pdf_name1 pdf_name2.pdf -o`
  
**2) For easier experience, use the ExecPdfEditor.bat :**
- Put yours pdf files in the same folder as your Python and executable and follow next exemple :
<br>2.1)If you need to edit from only one pdf : <br>
 - Command : `ExecPdfEditor.bat pdf_name1.pdf` 
<br> 2.2)From 2 or more : <br>
  - Command : `ExecPdfEditor.bat pdf_name1.pdf pdf_name2.pdf`



