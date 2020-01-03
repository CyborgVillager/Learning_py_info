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


def driver_name(driver_name):
    driver_name = input('Enter driver name: ')
    return driver_name

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
    return car_color


def car_model(car_model):
    car_model = input('What is the car\'s model? ')
    return car_model


def is_sov_regan_era(is_sov_regan_era):

    while True:
        is_sov_regan_era = input(' Is this car part of the Regan/ Soviet era?' + '\n'
                                 + ' Type Yes or No to proceed.' + '\n' +
                                 'Thank you. ').capitalize()
        try:
            if is_sov_regan_era == 'Yes':
                return is_sov_regan_era
            elif is_sov_regan_era == 'No':
                return is_sov_regan_era

        except TypeError:
               print('Please type Yes or No to continue.')


def space():
    space =  print('\n')

def under_line_result_info():
    print('---------------- ----------------  DRIVER CAR INFO - BASIC DATA ---------------- ' +
          '---------------- ---------------- ')

def under_line_result():
    print('---------------- ---------------- ---------------- ---------------- ----------------' +
          '---------------- ----------------')


def car_Info(driver_name,car_color,car_model,is_sov_regan_era ):

    driver_name = driver_name(driver_name)
    car_color = car_color(car_color)
    car_model = car_model(car_model)
    is_sov_regan_era = is_sov_regan_era (is_sov_regan_era)
    car1 = Car(driver_name,car_color,car_model,is_sov_regan_era)

    space()
    under_line_result_info()

    print('The driver\'s name is ' + yellow + car1.getDriver_Name() + end + ' The car color is ' + car1.getCar_Color() +
          end + ' The car model is ' + underline + yellow + car1.getCar_Model() + end +
          ' The car is part of the Soviet/Regan Era: ' + bold + underline + yellow +
          str(car1.getIs_Sov_Regan_Era()) + end)

    under_line_result()

car_Info(driver_name,car_color,car_model,is_sov_regan_era )