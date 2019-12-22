class Car:
    def __init__(self, year, make, model):
        self.__year = year
        self.__make = make
        self.__model = model


    def getYear(self):
        return self.__year


    def getMake(self):
        return self.__make


    def getModel(self):
        return self.__model

    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color = color

def main():
    a_Car = Car('Black', '1999','Audi','A6')
    a_Car1 = Car('Yellow')
    print('the car color is', a_Car.getColor(), 'The car year is', a_Car.getYear(),'the cars name is ', \
          a_Car.getMake(), 'the car model is ', a_Car.getModel())


main()

#include string function after calss 