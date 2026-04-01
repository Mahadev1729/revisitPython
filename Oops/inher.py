# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object
d = Dog()

d.speak()   # inherited from Animal
d.bark()    # own method
