print('To samo co Laboratorium 2 -> Zadanie 1')
print('')

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
    
