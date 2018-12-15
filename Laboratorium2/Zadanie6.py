# Przygotuj słownik zawierający obce wyrazy oraz ich możliwe znaczenia. Pobierz
# od użytkownika dane w formacie: wyraz obcy: znaczenie1, znaczenie2, ... itd.
# Pobieranie danych kończy wpisanie słowa “koniec”. Podane dane zapisz w pliku.
# Użytkownik powinien mieć możliwość dodawania nowych i zmieniania
# zapisanych danych.

def intro():
    print("1: Dodaj słowo do słownika")
    print("2: Czytaj słownik")
    print("3: Szukaj słowa:")

slownik_path = 'dict.txt'

fle = open(slownik_path, "a+")
print("Otwarto słownik")
intro()
act = input("Podaj akcje")
if act == '1':
    foreign = input("Podaj słowo obce")
    c = 1
    znaczenia = []
    while True:
        znaczenie = input("Podaj znaczenie" + str(c))
        if znaczenie == 'koniec':
            break
        else:
            znaczenia.append(znaczenie)
    fle.write(foreign + ": ")
    for znaczenieee in znaczenia:
        fle.write(znaczenieee + ", ")
    fle.write("\n\n")

else:
    fle.close()
    quit(0)




