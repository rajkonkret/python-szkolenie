class Mem:
    def __init__(self, name, url, is_favorite=False):
        self.name = name
        self.url = url
        self.is_favorite = is_favorite

m = Mem('programowanie jest suuuper','http://super.jpg')
m2 = Mem('Jestem Bo','http://aa.jpg', True)

print(m2.is_favorite)
print(m.is_favorite)
mems = [m,m2]
mems.append(m)
mems.append(Mem('Python jest jest jaki jest','htttp:/'))
print(mems)
for mem in mems:
    if mem.is_favorite:
        print(mem.name,mem.url)
