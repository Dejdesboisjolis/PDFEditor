@echo off
rem python PdfMerger.py -p %*
set /P choice=Taper 1-Merger des pdfs 2-Extraire des pages d'un pdf 3-Supprimer des pages d'un pdf: 
:switch-case

  :: Call and mask out invalid call targets
  goto :switch-case-N-%choice% 2>nul || (
    :: Default case
    echo Something else
  )
  goto :switch-case-end

:switch-case-N-1
    START %cd%\PdfMerger.exe -p %* -o m
    goto :switch-case-end 

:switch-case-N-2
    SET /P selection=Mode de selection pg -Selectionner une ou plusieurs page ------ rg -Selectionner une plage de page (format :min max):
    echo %selection%
    SET /P page=Tapez le numero des pages que vous souhaitez extraire, suivi d'un espace entre chaque:
    START %cd%\PdfMerger.exe -p %~1 -o e -%selection% %page%
    goto :switch-case-end 

:switch-case-N-3
    SET /P selection=Mode de selection 1-Selectionner une ou plusieurs page 2-Selectionner une plage de page (format :min max):
    SET /P page=Tapez le numero des pages que vous souhaitez supprimer, suivi d'un espace entre chaque: 
    START %cd%\PdfMerger.exe -p %~1 -o d -%selection% %page%
    goto :switch-case-end

:switch-case-end
   echo After Switch/case 