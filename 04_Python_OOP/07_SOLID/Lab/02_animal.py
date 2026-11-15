class Animal:
    @staticmethod
    def make_sound():
        pass

class Cat(Animal):
    @staticmethod
    def make_sound():
        print("meow")

class Dog(Animal):
    @staticmethod
    def make_sound():
        print("woof-woof")

class Chicken(Animal):
    @staticmethod
    def make_sound():
        print("chicken sound")

def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

cat = Cat()
dog = Dog()
chicken = Chicken()
animals = [cat, dog, chicken]
animal_sound(animals)