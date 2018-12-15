import math
a = int(input("Podaj bok a"))
b = int(input("Podaj bok b"))
c = int(input("Podaj bok c"))

def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def prostokatny(a, b, c):  #to powinno zaifowac sie trzy razy zeby bylo dobrze
    if (a*a + b*b) == c*c:
        return True
    else:
        return False

if a < b+c  and b < a+c  and c < a+b :
    print("Można zbudowac trojakt")
    print("Obwód = " + str(a + b + c))
    print("Pole = " + str(heron(a, b, c)))
    print("Prostokątny: " + str(prostokatny(a, b, c)))

else:
    print("Nie mozna zbudowac trojkata")
