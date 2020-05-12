import matplotlib.pyplot as plt
a,b =2,1
x = range(-5, 5)

y = [] # lista wartości
for i in x:
    y.append(a * i + b)
plt.plot(x, y)
plt.title('Wykres f(x) = a*x + b')
plt.grid(True)
y = []
x = range(-5,15)
for i in x:
    y.append(i*i)
plt.plot(x,y)
y.clear()
print(y)
x = range(-10,15)
for i in x:
    y.append(3*i+15)
plt.plot(x,y)
plt.show()