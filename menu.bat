@echo off
cd C:\Users\bunnv\Desktop\STUDIA\3 SEM\Skrypty\Python\Projekt\Scuba-Diver
:menu
cd C:\Users\bunnv\Desktop\STUDIA\3 SEM\Skrypty\Python\Projekt\Scuba-Diver
cls
echo  ====================================================================
echo                                 MENU                               
echo  ====================================================================
echo.                                                                        
echo  Wybierz jedna z ponizszych opcji wprowadzajac odpowiednia cyfre:                                
echo  1. Start                                                        
echo  2. Backup                                                         
echo  3. Informacje o programie                                              
echo  4. Wyniki programu                                                
echo  5. Zakoncz                                                                                             
echo  ====================================================================
echo.
set /p choice="Wybierz opcje[1-5]: "

IF %choice%==1 GOTO startt
IF %choice%==2 GOTO backup
IF %choice%==3 GOTO info
IF %choice%==4 GOTO html
IF %choice%==5 GOTO exit

echo.
echo Wybierz jedna z podanych opcji.
pause
GOTO :menu

:startt
cls
python main.py
pause
GOTO :menu

:backup
cls
cd C:\Users\bunnv\Desktop
mkdir Backup-%date%
xcopy "C:\Users\bunnv\Desktop\STUDIA\3 SEM\Skrypty\Python\Projekt\Scuba-Diver" C:\Users\bunnv\Desktop\Backup-%date% /E /H /C /I
echo Backup wykonany pomyslnie, backup znajduje sie na pulpicie.
pause
GOTO :menu

:info
cls
echo.
echo  ====================================================================
echo               INFORMACJE O PROGRAMIE I JEGO DZIALANIE               
echo  ====================================================================
echo.
echo  Zadaniem programu Scuba-Diver jest dobranie takich zestawow dla ple-
echo  -twonurka, by spelnialy one wszystkie wymagania a przy tym zeby ich
echo  waga byla jak najmniejsza.
echo.
echo  Kazdy zestaw sklada sie z nastepujacych elementow:
echo  - tlenu
echo  - azotu
echo  - wagi
echo.
echo  W pliku wejsciowym mamy zadane wymagania czyli:
echo  - minimalna ilosc tlenu
echo  - minimalna ilosc azotu
echo.
echo  Program na podstawie tych wymagan dobierze takie zestawy by spelni-
echo  -ly one wszystkie wymagania i wazyly przy tym jak najmniej.
echo  ====================================================================
echo                               DANE WEJSCIOWE               
echo.
echo   Dane wejsciowe sa zapisywane w folderze Inputs, dla kazdego zestawu
echo   mamy osobny plik wejsciowy input[x].txt, gdzie x to numer zestawu.

echo   Przykladowy zestaw wyglada nastepujaco:
echo. 
echo    5 60        #wymagana ilosc tlenu, wymagana ilosc azotu
echo    5           #zadeklarowana liczba zestawow
echo    3 36 120    #ilosc tlenu, ilosc azotu, waga zestawu
echo    10 25 129
echo    5 50 250
echo    1 45 130
echo    4 20 119
echo.
echo    W ten sam sposob zapisany jest kazdy inny plik wejsciowy.
echo.
echo.
echo  ====================================================================
echo                               DANE WEJSCIOWE               
echo   Dane wyjsciowe sa zapisywane w folderze Outputs, dla kazdego zestawu
echo   mamy osobny plik wyjsciowy output[x].txt, gdzie x to numer zestawu.
echo.
echo   W kazdym pliku jest zapisana liczba, ktora jest minimalna z wag zestawow.
echo.
echo.
echo  ====================================================================
echo  Autor programu: Wojciech Krolik, Informatyka II rok, grupa: 3E
echo.
echo.
pause
GOTO :menu

:html
cls
cd "C:\Users\bunnv\Desktop\STUDIA\3 SEM\Skrypty\Python\Projekt\Scuba-Diver"
start index.html
GOTO :menu

:exit
exit
