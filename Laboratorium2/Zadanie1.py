# Napisz program, który wypisuje liczby od START do STOP w kroku zadanym przez
# użytkownika. Umożliw użytkownikowi wprowadzenie liczby początkowej, liczby
# końcowej i wielkości odstępu między kolejnymi liczbami.

start=input("Podaj liczbę startową")
stop=input("Podaj liczbę końcową")
spc=input("Podaj ilość odstępu")

for x in range(int(start),int(stop)):
    print(x, end='')
    for y in range(0,int(spc)):
        print(' ', end='')