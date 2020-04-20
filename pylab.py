import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 2
x = range(-100, 11) # lista argumentów x
y = [] # lista wartości
for i in x:
    y.append(a * i + b)
plt.plot(x, y)
plt.title('Wykres f(x) = a*x - b')
plt.grid(False)
plt.show()