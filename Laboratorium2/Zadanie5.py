# Napisz program, który umożliwi wprowadzanie ocen z podanego przedmiotu,
# następnie policzy i wyświetla średnią, medianę i odchylenie standardowe
# wprowadzonych ocen. Funkcje pomocnicze i statystyczne umieść w osobnym
# module.

import Laboratorium2.zad5_lib as zad_lib
oceny = []
inp = 'a'
while inp != 'c':
    inp = input("Podaj Oceny, aby zakończyć wcisnij c")
    if inp != 'c':
        oceny.append(int(inp))
print(oceny)
print("Średnia: " + str(zad_lib.srednia(oceny)))
print("Mediana: " + str(zad_lib.mediana(oceny)))
print("Odchylenie: " + str(zad_lib.odchylenie(oceny)))