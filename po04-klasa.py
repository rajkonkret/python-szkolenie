class  HighSchool:
    def __init__(self, name, distance, points):
        self.name = name
        self.distance = distance
        self.points = points

schools = []
schools.append(HighSchool(name= 'lo zamoyskiego',distance=15,points=173))
schools.append(HighSchool(name= 'lo kopernika',distance=7,points=193))
schools.append(HighSchool(name= 'lo zoska',distance=6,points=182))
max_schhol = None
for school in schools:
    if school.points <= 180 and school.distance <= 10:
        if max_schhol:
            if school.points > max_schhol:
                max_schhol
        else:
            max_schhol = school

if max_schhol:
    print(max_schhol.name)
else:
    print('nie ma szkoły')