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
def main():
    a_Car = Car('1999','Audi','A6')
    a_Car1 = Car('2015','Ford','T90')
    print('The car year is', a_Car.getYear(),'the cars name is ', a_Car.getMake(), 'the car model is ', a_Car.getModel())
    print('The car year is', a_Car1.getYear(),'the cars name is ', a_Car1.getMake(), 'the car model is ', a_Car1.getModel())

main()