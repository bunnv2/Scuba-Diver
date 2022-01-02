 ====================================================================
              INFORMACJE O PROGRAMIE I JEGO DZIALANIE               
 ====================================================================

 Zadaniem programu Scuba-Diver jest dobranie takich zestawow dla ple-
 -twonurka, by spelnialy one wszystkie wymagania a przy tym zeby ich
 waga byla jak najmniejsza.

 Kazdy zestaw sklada sie z nastepujacych elementow:
 - tlenu
 - azotu
 - wagi

 W pliku wejsciowym mamy zadane wymagania czyli:
 - minimalna ilosc tlenu
 - minimalna ilosc azotu

 Program na podstawie tych wymagan dobierze takie zestawy by spelni-
 -ly one wszystkie wymagania i wazyly przy tym jak najmniej.
 ====================================================================
                              DANE WEJSCIOWE               

  Dane wejsciowe sa zapisywane w folderze Inputs, dla kazdego zestawu
  mamy osobny plik wejsciowy input[x].txt, gdzie x to numer zestawu.
  Przykladowy zestaw wyglada nastepujaco:
 
   5 60        #wymagana ilosc tlenu, wymagana ilosc azotu
   5           #zadeklarowana liczba zestawow
   3 36 120    #ilosc tlenu, ilosc azotu, waga zestawu
   10 25 129
   5 50 250
   1 45 130
   4 20 119

   W ten sam sposob zapisany jest kazdy inny plik wejsciowy.


 ====================================================================
                              DANE WEJSCIOWE               
  Dane wyjsciowe sa zapisywane w folderze Outputs, dla kazdego zestawu
  mamy osobny plik wyjsciowy output[x].txt, gdzie x to numer zestawu.

  W kazdym pliku jest zapisana liczba, ktora jest minimalna z wag zestawow.
