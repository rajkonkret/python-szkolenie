for i in range(1,26):
    print(str(i) + '.py')
    name = str(i) + '.py'
    file = open(name,'w')
    file.close()