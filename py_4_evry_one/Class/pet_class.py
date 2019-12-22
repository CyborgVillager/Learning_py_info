

class Pet:
    def __init__(self,name,animal_type,age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def setName(self,name):
        self.name = name

    def setAnimal_type(self,animal_type):
        self.animal_type = animal_type

    def setAge(self,age):
        self.age = age

    def getName(self):
        return self.name

    def getAnimal_type(self):
        return self.animal_type

    def getAge(self):
        return self.age

    def toData(self):
        return 'Your pet {} is a {} and is {} yrs old'.format(self.name,self.animal_type,self.age)

name = input('What is your pet name?')
animal_type = input('What is your pet species?')
age = int(input('How old is ' + name + ' ?'))

user_Pet = Pet(name,animal_type,age)
print(user_Pet.toData())