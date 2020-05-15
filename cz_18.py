name = 'C:\\Users\\user\\Documents\\Python szkolenie\\test.py'
file = open(name,'w')
file.close()
file = open(name,'r',encoding="utf-8")
for line in file:
    print(line)
file.close()