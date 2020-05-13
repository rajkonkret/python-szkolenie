import matplotlib.pyplot as p

x = range(-5, 6)
y = []

for i in x:
    y.append(3*i+1)
    
p.plot(x,y, color='gold')
p.show()
