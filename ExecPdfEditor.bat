@echo off
cls

rem python PdfMerger.py -p %*
set /P choice=Tapez : 1-Merger des pdfs   ---------    2-Extraire des pages d'un pdf   ---------   3-Supprimer des pages d'un pdf: 
:switch-case

  :: Call and mask out invalid call targets
  goto :switch-case-N-%choice% 2>nul || (
    :: Default case
    echo Something else
  )
  goto :switch-case-end

:switch-case-N-1
    START %cd%\PdfMerger.exe -p %* -o m
    echo la commande est : %cd%\PdfMerger.exe -p %* -o m
    rem goto :switch-case-end 

:switch-case-N-2
    SET /P selection=Tapez : pg -Selectionner une ou plusieurs page     ------    rg -Selectionner une plage de page (format :min max):
    IF NOT %selection% == pg IF NOT %selection% == rg (echo : syntaxe : erreur de saisie)
    SET /P page=Tapez le numero des pages que vous souhaitez extraire, suivi d'un espace entre chaque:
    START %cd%\PdfMerger.exe -p %~1 -o e -%selection% %page%
    echo  La commande est : %cd%\PdfMerger.exe -p %~1 -o e -%selection% %page%
    rem goto :switch-case-end 

:switch-case-N-3
    SET /P selection=Tapez : pg -Selectionner une ou plusieurs page     ------    rg -Selectionner une plage de page (format :min max):
    IF NOT %selection% == pg IF NOT %selection% == rg (echo : syntaxe : erreur de saisie)
    SET /P page=Tapez le numero des pages que vous souhaitez supprimer, suivi d'un espace entre chaque: 
    START %cd%\PdfMerger.exe -p %~1 -o d -%selection% %page%
    echo %cd%\PdfMerger.exe -p %~1 -o e -%selection% %page%
    rem goto :switch-case-end

:switch-case-end
   echo After Switch/case 