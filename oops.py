class Animal:
    def sound(self):
        print("WOOO...")


class Dog(Animal):
    def dogsound(self):
        print("Bow Bow....")



dog = Dog()
dog.dogsound()
dog.sound()