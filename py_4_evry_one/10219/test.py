class Car:
    def __init__(self):
        self.__year = '2010'
        self.__make = 'Audi'
        self.__model = 'A6'

    def getYear(self):
        return self.__year

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

def sayS():
    #default to call upon parent Car:
    defaultCarObject = Car()
    #obtain info from class car -> to its children year,make, and model
    print('Your car is an', defaultCarObject.getMake(), 'the year is' , \
          defaultCarObject.getYear(), 'the model is', defaultCarObject.getModel())
def main():

    sayS()




main()