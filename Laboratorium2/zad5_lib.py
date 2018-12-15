from math import sqrt

def srednia(lista_ocen):
    liczba_ocen = len(lista_ocen)
    return suma_ocen(lista_ocen) / liczba_ocen

def suma_ocen(lista_ocen):
    liczba_ocen = len(lista_ocen)
    suma = 0
    for ocena in lista_ocen:
        suma += ocena
    return suma

def mediana(lista_ocen):
    liczba_ocen = len(lista_ocen)
    cen = liczba_ocen // 2
    if liczba_ocen % 2 != 0:
        return lista_ocen[int(cen)]
    else:
        return srednia([lista_ocen[cen-1], lista_ocen[cen]])

def odchylenie(lista_ocen):
    avg = srednia(lista_ocen)
    kwadrat_suma = 0
    for ocena in lista_ocen:
        kwadrat_suma += pow(ocena - avg, 2)
    wariancja = kwadrat_suma/avg
    return sqrt(wariancja)



