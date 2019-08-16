class Animal:
    def bark(self):
        print('bark')


class Pet(Animal):
    def groom(self):
        print('groom')


animal = Animal()
animal.bark()

pet = Pet()
pet.bark()
