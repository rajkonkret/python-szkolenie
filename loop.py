import requests
import matplotlib.pyplot as plt
import seaborn

lm_json = requests.get('https://api.nbp.pl/api/cenyzlota/2020-05-20/2020-07-20').json()

x = []
y = []
x_label = []
counter = 0
print(len(lm_json))
for i in range(len(lm_json)):
    x_label.append((i %10) +1 )
    x.append(lm_json[i]['data']) #jak zrobic zeby zamiast dat, na osi x bylo powtarzane odliczanie od 1-10 az do konca wszystkich wartosci y
    y.append(lm_json[i]['cena'])

counter += 1

print('Ilość prob:',counter)



seaborn.set(style="darkgrid")

plt.xticks(
rotation=0,
horizontalalignment='right',
fontweight='bold',
fontsize=7
)
ax = plt.gca()
ax.set_xticklabels(x_label)
plt.plot(x,y,lw=2)
plt.show()