# Izračun zimske lige

## Nalaganje rezultatov
Rezultate v CSV obliki naložimo v direktorij ```Rezultati```. CSV mora biti v formatu OE2003. Lahko tudi OEvent-ova verzija OE2003.

## Začetno stanje
Začetno stanje je zabeleženo v ```Zacetek.txt``` in določa osnovno vrednost tekmovalcev pred začetkom lige. Temelji na izračunu zadnje lige. Novo začetno datoteko pripravimo s pomočjo ```nova_sezona.py```. Rezultat, ki je v datoteki ```zacetek1.txt``` preimenujte v ```Zacetek.txt```.

## Računanje
Poženeš skripto prvič. V ```Stanja_racunana``` se naložijo rezultati. Skopiraš jih v ResnaStanja, če so OK pustiš, kakor je, sicer popraviš, pri naslednjem poganjanju se naračuna še končni izračun na podlagi teh datotek.

## Opazke

* Če za kako tekmo ni rezultatov, moraš dati v ```Rezultati``` prazno datoteko s pravilnim imenom (sicer se na koncu v CSV ne izpišejo vsi stolpci, ampak toliko premalo, kolikor CSV datotek z rezultati manjka).