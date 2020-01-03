# pet name
# pet species
# pet age
# pet aquatic or land or hybrid
from text_color import *
class Pets:
    def __init__(self,pet_name,pet_species,pet_age,pet_aquatic_or_land_or_hybrid):
        self.pet_name = pet_name
        self.pet_species = pet_species
        self.pet_age = pet_age
        self.pet_aquatic_or_land_or_hybrid = pet_aquatic_or_land_or_hybrid


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
        self.pet_aquatic_or_land_or_hybrid
        return self.pet_aquatic_or_land_or_hybrid

def pet_name(pet_name):
    pet_name = input('What is your pet\'s name? ')
    return pet_name

def pet_species(pet_species,pet_name):
    pet_species = input('What is ' + pet_name + ' species? ')
    return pet_species

def pet_age(pet_age, pet_name):
    pet_age = input('How old is' + pet_name + '? ')
    return pet_age

def is_pet_aquatic_land_or_hybrid(pet_aquatic_or_land_or_hybrid, pet_name):
   pet_aquatic_or_land_or_hybrid = input('Is ' + pet_name + 'an' + bold + 'aquatic' + end +
                                          ' or' + bold + ' land' + end + ' animal? Or are they a ' +
                                          bold + 'hybrid? ')

def main(pet_name,pet_species,pet_age,is_pet_aquatic_land_or_hybrid):
    pet_name = pet_name(pet_name)
    pet_species = pet_species(pet_species,pet_name)
    pet_age = str(pet_age(pet_age,pet_name))
    is_pet_aquatic_land_or_hybrid = is_pet_aquatic_land_or_hybrid(is_pet_aquatic_land_or_hybrid,pet_name)
    main = Pets(pet_name,pet_species,pet_age,is_pet_aquatic_land_or_hybrid)

    print('Your pet name is ' + main.pet_name + 'species is' +  main.pet_species + main.pet_name + ' age is '
          + str(main.pet_age) + main.pet_name + ' is an ' + main.pet_aquatic_or_land_or_hybrid  + ' animal')

main(pet_name,pet_species,pet_age,is_pet_aquatic_land_or_hybrid)