# Napisz program, który pobierzeod użytkownika ilość ruchów
# jaką ma wykonać cząstka, a następnie narysuje
# wygenerowane losowo ruch tej cząstki

import matplotlib.pyplot as plt
import pylab as p
import numpy as np
import random

strile = input("Podaj ilość ruchów cząsteczki")
ile = int(strile)

x = y = 0
lx = [0]
ly = [0]
pierwszex = 0
pierwszey = 0
ostatniex = 0
ostatniey = 0

for i in range(0, ile):
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)
    y = y + np.sin(rad)
    lx.append(x)
    ly.append(y)
    if(i == 0):
        pierwszex = lx[0]
        pierwszey = ly[0]
    elif(i == ile - 1):
        ostatniex = lx[i]
        ostatniey = ly[i]

poczatek = [pierwszex, ostatniex]
koniec = [pierwszey, ostatniey]

s = np.fabs(np.sqrt(x**2 + y**2))
print("Wektor przesunięcia: ", s)

plt.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
plt.xlabel("lx")
plt.ylabel("ly")
plt.title("Ruchy Browna")
plt.grid(True)
plt.plot(poczatek,koniec)
plt.show()