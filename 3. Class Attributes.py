######CLASS ATTRIBUTES################
#Not specific to an object of the class, but specific to the class directly

class Person:
    number_of_people = 0  #This is a class attribute, does not use self, no access to an instance of the class

    def __init__(self, name):
        self.name = name #Here, the name is different for each instance of the class because of the self argument
        Person.number_of_people += 1 #when a new Person is created it is added to the number_of_people
p1 = Person("Bill")
p2 = Person("Jill")

print(p1.number_of_people) #returns 0 because not specific to p1

Person.number_of_people = 8 #can be changed at the Class level
print(p1.number_of_people) #and THEN it influences this result, because it is part of the class and still not specific to p1
print(p2.number_of_people)

print(Person.number_of_people)

