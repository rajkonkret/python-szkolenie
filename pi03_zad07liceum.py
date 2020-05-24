class HighScool:
    def __init__(self,name, min_points, distance):
        self.name = name
        self.min_points = min_points
        self.distance = distance
    def __repr__(self):
        return self.name + ' needs ' + str(self.min_points) + ' point and is ' + str(self.distance) + ' km away.'

first_hs = HighScool('lo zamoyuski', 173,15)
second_hs = HighScool('LO MK',193,7)
third_hs = HighScool('LO Zoska',122,6)

scools = []
scools.append(first_hs)
scools.append(second_hs)
scools.append(third_hs)

for i in scools:
    print(i)

