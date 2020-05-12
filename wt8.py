dictionary = {}
dictionary["first"] = "pierwszy"
dictionary["dog"] = "pies"
dictionary["hot"] = "gorący"
dictionary["sun"] = "słońce"
print(dictionary["first"])

for i,v in enumerate(dictionary):
    print(dictionary[v], i)

for i in dictionary:
    print(i," ", dictionary[i])