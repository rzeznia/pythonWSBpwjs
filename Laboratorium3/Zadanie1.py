import matplotlib.pyplot as plt
import pylab as p
import numpy as np

stra = input("Podaj a funkcji: ")
strb = input("Podaj b funkcji: ")
a = int(stra)
b = int(strb)

x = p.arange(-10, 12.5, 2.5)
y=a*x+b
plt.plot(x, y, label="Funkcja Liniowa")
plt.xlabel("Oś x")
plt.ylabel("Oś y")
plt.title("Wykres f(x) = ax + b")
plt.legend()
plt.grid(True)
if(a > 0):
    plt.text(1,2,'Funkcja rosnąca')
else:
    plt.text(1,2,'Funkcja malejąca')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()