import random

feet_in_mile = 5280
meters_in_kilometer = 1000
ja_bros = ['Jonathan Almawi', 'Joshua Almawi', 'Jacob Almawi', 'Jonah Almawi']

def get_file_extension(filename):
    return filename[filename.index('.') + 1: ]

def roll_dice(numb):
    return  random.randint(1,numb)

# https://docs.python.org/3/py-modindex.html

