################################################################################
#############Inheritance#########################


class Pet: #General class
    def __init__(self, name, age):
         self.name = name
         self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")



class Cat(Pet): # Specific class, no need to init to inehrit from PET
    def __init__(self, name, age, color):
        super().__init__(name, age) #super() references the super class, here, Pet. self doen't need to be passed
        self.color = color
    
    def speak(self): #Overrides what the general class does, because has the same function name
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass


p = Pet("Tim", 19)
p.show()
p.speak()

c = Cat("Bill", 14, "Red")
c.show()
c.speak()

d = Dog("Jill", 20)
d.show()
d.speak()

f = Fish("Bubbles", 10)
f.speak()
