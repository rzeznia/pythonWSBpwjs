# Napisz program, który wypisuje liczby od START do STOP w kroku zadanym przez
# użytkownika. Umożliw użytkownikowi wprowadzenie liczby początkowej, liczby
# końcowej i wielkości odstępu między kolejnymi liczbami.

start=input("Podaj liczbę startową")
stop=input("Podaj liczbę końcową")
spc=input("Podaj ilość odstępu")
step = int(spc)

for x in range(int(start),int(stop)+1):
    if step != 1:
        if x % step == 0:
            print(x , end=' ')
    else:
        print(x , end=' ')
    
