import matplotlib.pyplot as plt
import pylab as p
import numpy as np

x1 = p.arange(0,10,1)
y1 = x1*2

x2 = p.arange(0,10,1)
y2 = x2

x3 = p.arange(0,10,1)
y3 = 0.5*x3*0.5*x3+x3+2
plt.plot(x1, y1, color='blue',linewidth=2, linestyle='-.')
plt.plot(x2, y2, color='green',linewidth=3, linestyle=':')
plt.plot(x3, y3, color='red',linewidth=1, linestyle='-')

plt.xlabel("OŚ x")
plt.ylabel("OŚ y")

plt.title("Trzy różne wykresy")
plt.grid(True)


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.plot(x1, y1, color="blue",linewidth=2, linestyle="-.",label="x")
plt.plot(x2, y2, color="green",linewidth=3, linestyle=":",label="liniowy")
plt.plot(x3, y3, color="red",linewidth=1, linestyle="-",label="x**2")

plt.legend(loc='upper left')

plt.show()