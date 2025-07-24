#Methods relying on double underscores like __init__, __add__, __mul__, etc.

#In order to see dunder methods for a class, use dir() function

print("############################# INT Dunder Methods")
print(dir(int))

class Microwave:
    def __init__(self, brand, power_rating):
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on = False

    def __add__(self, other): #for an addition operand
        return f'{self.brand} + {other.brand}' #In order to define which operator to use for the fstring

    def __mul__(self, other):
        return f'{self.brand} likes {other.brand}'

    def __str__(self): #returns user friendly info
        return f'{self.brand} (Rating : {self.power_rating})' 

    def __repr__(self): #returns useful info for dvlp
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'


smeg = Microwave("Smeg", "B")
bosch = Microwave("Bosch", "A")


print(smeg + bosch) #Impossible without the __add__ dunder method
print(smeg * bosch) #Requires the __mul__ dunder method
print(smeg) #Requires the __str__ to provide legible information instead of the memory address
print(bosch)
print(repr(smeg)) #Gives more specific information
print(repr(bosch))


