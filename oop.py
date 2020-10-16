#Simple program representing Object Oriented Programming in Python

#Parent Class Animal
class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

#Child Class that Inherited from Animl
class Dog(Animal):
    #class atributes
    species = "Canis Familiaris"

    def __init__(self, species, name, age, breed, sound):
        self.breed = breed
        self.sound = sound
        #We can use init function from Animal Class
        super().__init__(species, name, age)

    #This function needs to be called using "." operator
    def description(self):
        return f"{self.name} is {self.age} years old."

    #This function returns f-string, which means that
    #operation print(DogObject) will show the following
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def speak(self):
        return f"{self.name} says {self.sound}!"



#------------------------MAIN-----------------------#
if __name__ == "__main__" :

    newDog = Dog("Dog", "Alex", 12, "daschshund", "woof woof")  #New Dog instance
    print(newDog.description())
    print(newDog)

    print(newDog.speak())
