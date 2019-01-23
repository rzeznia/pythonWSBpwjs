# Napisz program, który pyta o wartości [a] i [b] i przedstawia postać
# równania liniowego z tymi parametrami.
# Podaj a: 4
# Podaj b: 6
# y = 4 x + 6
# • Rozbuduj program 2 tak by przedstawiał jaka będzie wartość zmiennej
# [y] w zależności od wartości [x] – którą podaje użytkownik.
# Podaj a: 4
# Podaj b: 3
# y = 4 x + 3
# dla x = 5 wartość y = 23

stra = input("Podaj A równania liniowego")
strb = input("Podaj B równania liniowego")
a = int(stra)
b = int(strb)
print('Postać równania liniwoego: y = ' + stra + 'x + ' + strb)
strx = input('Podaj wartosć x: ')
x = int(strx)
print('Dla x = ' + strx + ' wartość y = ' + str(a*x+b))