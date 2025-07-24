# Class METHODS

class Flower:
    number_of_flowers = 0  

    def __init__(self, name):
        self.name = name
        Flower.add_flower()

    @classmethod #In order to denote what is going on
    def number_of_flowers_(cls):
        return cls.number_of_flowers #This is not going to be specific to one instance of the class

    @classmethod
    def add_flower(cls):
        cls.number_of_flowers += 1

f1 = Flower("Daffodil")
f2 = Flower("Rose")

print(Flower.number_of_flowers_())

