# pet name
# pet species
# pet age
# pet aquatic or land or hybrid
from text_color import *


class Pets:
    def __init__(self, pet_name, pet_species, pet_age, is_pet_aquatic_or_land_or_hybrid):
        self.pet_name = pet_name
        self.pet_species = pet_species
        self.pet_age = pet_age
        self.is_pet_aquatic_or_land_or_hybrid = is_pet_aquatic_or_land_or_hybrid

    def getPet_Name(self):
        self.pet_name
        return self.pet_name

    def getPet_Species(self):
        self.pet_species
        return self.pet_species

    def getPet_Age(self):
        self.pet_age
        return self.pet_age

    def getPet_Aquatic_or_Land_Or_Hybrid(self):
        self.is_pet_aquatic_or_land_or_hybrid
        return self.is_pet_aquatic_or_land_or_hybrid


def pet_name(pet_name):
    pet_name = input('What is your pet\'s name? ').capitalize()
    return pet_name


def pet_species(pet_species, pet_name):
    pet_species = input('What is ' + pet_name + ' species? ')
    return pet_species


def pet_age(pet_age, pet_name):
    pet_age = input('How old is ' + pet_name + '? ')
    return pet_age

def space():
    print('\n')

def is_pet_aquatic_land_or_hybrid(is_pet_aquatic_land_or_hybrid, pet_name):
    while True:
        is_pet_aquatic_land_or_hybrid = input('Is ' + pet_name + ' an ' + bold + 'aquatic ' + end +
                                                ' or' + bold + ' land' + end + ' animal? Or are they a ' +
                                                 bold + 'hybrid? ').lower()
        try:
            if is_pet_aquatic_land_or_hybrid == 'land':
                return is_pet_aquatic_land_or_hybrid
            elif is_pet_aquatic_land_or_hybrid == 'aquatic':
                return is_pet_aquatic_land_or_hybrid
            elif is_pet_aquatic_land_or_hybrid == 'hybrid':
                return is_pet_aquatic_land_or_hybrid
            else:
                space()
                print('You must type either if  ' + pet_name + 'is an aquatic, land or hybrid animal: ')
        except TypeError:
                print('You must type either if  ' + pet_name + 'is an aquatic, land or hybrid animal: ')


def main(pet_name, pet_species, pet_age, is_pet_aquatic_land_or_hybrid):
    pet_name = pet_name(pet_name)
    pet_species = pet_species(pet_species, pet_name)
    pet_age = str(pet_age(pet_age, pet_name))
    is_pet_aquatic_land_or_hybrid = is_pet_aquatic_land_or_hybrid(is_pet_aquatic_land_or_hybrid, pet_name)
    main = Pets(pet_name, pet_species, pet_age, is_pet_aquatic_land_or_hybrid)

    print('Your pet\'s name is ' + yellow + main.pet_name + end + '. It\'s species is ' + red + main.pet_species + end +
            '. ' + yellow + main.pet_name + '\'s' + end + ' age is ' +  red + str(main.pet_age) + end + ' years old. '
          + yellow + main.pet_name + end + ' is an ' + red +
          main.is_pet_aquatic_or_land_or_hybrid + end  + ' animal')


main(pet_name, pet_species, pet_age, is_pet_aquatic_land_or_hybrid)
