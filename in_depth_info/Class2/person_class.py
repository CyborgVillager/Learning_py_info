# person name
# person age
# person height
# person gender
# person fav color

from text_color import *

# Person Class
class Person:
    def __init__(self, person_name, person_age, person_height, person_gender, person_fav_color):
        self.person_name = person_name
        self.person_age = person_age
        self.person_height = person_height
        self.person_gender = person_gender
        self.person_fav_color = person_fav_color

    def getPerson_name(self):
        self.person_name
        return self.person_name

    def getPerson_Age(self):
        self.person_age
        return self.person_age

    def getPerson_Height(self):
        self.person_height
        return self.person_height

    def getPerson_Gender(self):
        self.person_gender
        return self.person_gender

    def getPerson_Fav_Color(self):
        self.person_fav_color
        return self.person_fav_color


# the persons name
def person_name(person_name):
    person_name = input('Enter the person\'s name: ').capitalize()
    return person_name


# the persons age
def person_age(person_age, person_name):
    person_age = int(input('Enter ' + person_name + '\'s age: '))
    return person_age


# the persons height
def person_height(person_height, person_name):
    feet = int(input(('Enter ' + person_name + '\'s height in inches: ')))
    person_height = ('{0:.2f}'.format(feet / 12))
    return person_height

def space():
    print('\n')

# the persons gender
def person_gender(person_gender, person_name):
    while True:
        person_gender = input('Is ' + person_name + ' a male or female? ').lower()

        try:
            if person_gender == 'male':
                return person_gender
            elif person_gender == 'female':
                return person_gender
            else:
                space()
                print('You must type either a ' + bold + 'male ' + end + 'or ' + bold + 'female' + end)
        except TypeError:
            print('You must type either a ' + bold + 'male ' + end + ' or ' + bold + 'female' + end)


# the person favorite color
def person_fav_color(person_fav_color, person_name):
    person_fav_color = input('What is ' + person_name + '\'s favorite color? ')

    if person_fav_color == 'red':
        person_fav_color = red + 'red'
    elif person_fav_color == 'purple':
        person_fav_color = purple + 'purple'
    elif person_fav_color == 'cyan':
        person_fav_color = cyan + 'cyan'
    elif person_fav_color == 'blue':
        person_fav_color = blue + 'blue'
    elif person_fav_color == 'green':
        person_fav_color = green + 'green'
    elif person_fav_color == 'yellow':
        person_fav_color = yellow + 'yellow'
    elif person_fav_color == 'dark cyan' or person_fav_color == 'darkcyan' or person_fav_color == 'dark_cyan':
        person_fav_color = dark_cyan + 'dark cyan'
    else:
        person_fav_color = unknown_color

    return person_fav_color


# Aquire necass info to combine into main func
def person_Info(person_name, person_age, person_height, person_gender, person_fav_color):
    person_name = person_name(person_name)
    person_age = person_age(person_age, person_name)
    person_height = person_height(person_height, person_name)
    person_gender = person_gender(person_gender, person_name)
    person_fav_color = person_fav_color(person_fav_color, person_name)
    person_info = Person(person_name, person_age, person_height, person_gender, person_fav_color)

    # Result info on the terminal
    space()
    print(yellow + person_info.person_name + '\'s ' + end + 'age is ' +
          combo_underline_yellow + str(person_info.person_age) + end + ' years old. ' + person_name + '\'s height is '
          + combo_underline_yellow + str(person_info.person_height) + end +' feet. ' + person_name + '\'s gender is '
          + combo_underline_yellow + person_info.person_gender + end + ' their favorite color is '
          + bold + person_fav_color)

# Result
person_Info(person_name, person_age, person_height, person_gender, person_fav_color)
