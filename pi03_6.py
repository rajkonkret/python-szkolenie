class Apartment:
    def __init__(self,dict):
        self.city = dict['city']
        self.price_per_meter = dict['price_per_meter']
        self.area = dict['area']
    def get_full_price(self):
        return round(self.area * self.price_per_meter * 0.95,2)
    def print_description(self):
        print(self.city, self.get_full_price())
    def __repr__(self):
        return self.city + ' ' + str(self.get_full_price())

apartment = Apartment({'city':'Warszawa',"price_per_meter":10,'area':50.29})
print(apartment.city)
print(apartment.get_full_price())
apartment.print_description()
apartament2 = Apartment({'city': 'Krakow','price_per_meter': 8,'area': 70.00})
apartament2.print_description()
print(apartment)