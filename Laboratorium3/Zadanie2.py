# Wykonaj wykres funkcji:
# • f(x) = x/(-3) + a dla x <= 0,
# • f(x) = x*x/3 dla x >= 0,
# • gdzie x = <-10;10> z krokiem 0.5.
# Współczynnik a podajeużytkownik. Na jednymwykresie. Wstaw tytuł wykresu,
# nazwy osi, legendę oraz wypozycjonuj osie liczbowe

import matplotlib.pyplot as plt
import pylab as p
import numpy as np

stra = input("Podaj a funkcji: ")
a = int(stra)

x1 = p.arange(-10, 0, 0.5)
x2 = p.arange(0, 10, 0.5)
y1=x1/-3+a
y2=x2*x2/3
y1
plt.plot(x1,y1, 'b', x2,y2,'r')
plt.xlabel("Oś x")
plt.ylabel("Oś y")
plt.title("Wykresy funkcji")
plt.legend(('y=x/-3+a', 'y=x*x/3'))
plt.grid(True)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()