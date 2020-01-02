from text_color import *
# driver name
# car color
# the car make
# car model #
# Sov / Regan Era


class Car:
    def __init__(self, driver_name, car_color,car_model,is_sov_regan_era):
        self.driver_name = driver_name
        self.car_color = car_color
        self.car_model = car_model
        self.is_sov_regan_era = is_sov_regan_era

    def getDriver_Name(self):
        self.driver_name
        return self.driver_name


    def getCar_Color(self):
        return self.car_color

    def getCar_Model(self):
        return self.car_model

    def getIs_Sov_Regan_Era(self):
        return self.is_sov_regan_era



driver_name = input('Enter driver name: ')

def car_color(car_color):
    car_color = input('What is the car\'s color? ').lower()

    if car_color == 'red':
        car_color = red + 'red'
    elif car_color == 'purple':
        car_color = purple + 'purple'
    elif car_color == 'cyan':
        car_color = cyan + 'cyan'
    elif car_color == 'blue':
        car_color = blue + 'blue'
    elif car_color == 'green':
        car_color = green + 'green'
    elif car_color == 'yellow':
        car_color = yellow + 'yellow'
    elif car_color == 'dark cyan' or car_color == 'darkcyan' or car_color == 'dark_cyan':
        car_color = dark_cyan + 'dark cyan'
    else:
        car_color = unknown_color
    car_color = car_color
    return car_color






def car_Info(car_color):
    car_model = input('What is the car\'s model? ')
    is_sov_regan_era = input(' Is this car part of the regan/ soviet era?' + '\n'
                             + ' Type Yes or No to proceed.' + '\n' +
                             'Thank you. ')

    car_color = car_color(car_color)
    car1 = Car(driver_name,car_color,car_model,is_sov_regan_era)
    print('The driver\'s name is ' + yellow + car1.getDriver_Name() + end + ' The car color is ' + car1.getCar_Color() +
          end + ' The car moel is ' + car1.getCar_Model() + ' The car is part of the Soviet/ Regan Era? ' +
          yellow + car1.getIs_Sov_Regan_Era() + end)






car_Info(car_color)