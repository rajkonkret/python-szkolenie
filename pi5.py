name ='Justyna'
i = 1
print(name[i])
print(len(name))
length = len(name)
for i in range(0,length):
    print(name[i])

for index,value in enumerate(name):
    print(index, value)

print("trzeci")
for i in name:
    print(i)