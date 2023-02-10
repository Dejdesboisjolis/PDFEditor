@echo off
rem python PdfMerger.py -p %*
set /P choice= Taper 1-Merger des pdfs, 2-Extraire des pages d'un pdf, 3-Supprimer des pages d'un pdf: 
:switch-case

  :: Call and mask out invalid call targets
  goto :switch-case-N-%choice% 2>nul || (
    :: Default case
    echo Something else
  )
  goto :switch-case-end

:switch-case-N-1
    echo tu as tape %choice% %~1
    START %cd%\PdfMerger.exe -p %* -o m
    goto :switch-case-end 

:switch-case-N-2
    echo tu as tape %choice% %~1
    SET /P page= Tapez le numero des pages que vous souhaitez extraire, suivi d'un espace entre chaque:
    echo tu as tape %page%
    START %cd%\PdfMerger.exe -p %~1 -o e -pg %page%
    goto :switch-case-end 

:switch-case-N-3
    echo tu as tape %choice% %~1
    SET /P page= Tapez le numero des pages que vous souhaitez supprimer, suivi d'un espace entre chaque: 
    echo tu as tape %page%
    START %cd%\PdfMerger.exe -p %~1 -o d -pg %page%
    goto :switch-case-end

:switch-case-end
   echo After Switch/case 