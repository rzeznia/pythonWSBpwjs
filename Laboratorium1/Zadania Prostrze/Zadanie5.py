# Napisz program, który pyta o 3 parametry i przedstawia postać równania
# kwadratowego z tymi parametrami.
# Podaj a: 2
# Podaj b: 3
# Podaj c: 4
# y = 2 x^2+ 3 x + 4
# • Rozbuduj program tak by obliczał DELTĘ
# Podaj a: 2
# Podaj b: 6
# Podaj c: 1
# y = 2 x^2+ 6 x + 1
# Delta wynosi: 28

import math

stra = input("Podaj A równania kwadratowego: ")
strb = input("Podaj B równania kwadratowego: ")
strc = input("Podaj C równania kwadratowego: ")
a = int(stra)
b = int(strb)
c = int(strc)
print('Postać równania kwadratowego: y = ' + stra + 'x^2 + ' + strb + 'x + ' + strc)
delta = b*b-(4*a*c)
print("Delta: " + str(delta))
if(delta > 0):
    print('x1 = ' + str( (-1 * b - math.sqrt(delta) ) / 2 * a) )
    print('x2 = ' + str( (-1 * b + math.sqrt(delta) ) / 2 * a) )
elif(delta == 0):
    print('x1 = ' + str(-1*b/2*a))
else:
    print('Delta ujemna, brak rozwiązań')