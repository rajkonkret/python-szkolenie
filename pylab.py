import numpy as np
import matplotlib.pyplot as plt
a = 2
b = 1
x = range(-10, 11) # lista argumentów x
y = [] # lista wartości
for i in x:
    y.append(a * i + b)
plt.plot(x, y)
plt.title('Wykres f(x) = a*x + b')
plt.grid(True)
plt.show()