# making a dictio maps englihs to spanish words
# importing from spanish_numb_info

# install PyDictionary
# exception error list: https://www.programiz.com/python-programming/exceptions

"""''''''
from PyDictionary import PyDictionary

english_to_spanish = PyDictionary()
print(english_to_spanish.translate("Range",'es'))
''''''"""

# english_to_spanish = dict()
english_to_spanish = {'one': 'uno', 'two': 'dos', 'three': 'tres', 'four': 'cuatro', 'five': 'cinco', 'six': 'seis',
                      'seven': 'siete', 'eight': 'ocho', 'nine': 'nueve', 'ten': 'diez'}


def spanish_func0():
    try:
        print(english_to_spanish)
        # index the dicto using the keys
        print(english_to_spanish['three'])

        # in operator -> tells you if something appears a key in the dictio
        # check if the key is in the dictio
        check_if_key_in_dictio = 'three'
        if check_if_key_in_dictio in english_to_spanish:
            print('yes the key --', check_if_key_in_dictio, '-- is not in the dicto')
        else:
            print('No the key --', check_if_key_in_dictio, '-- is not in the dictio')

    except KeyError:
        print('not in dicto, please try again!')


# spacing between the statements
def spacing():
    space_time = 1
    print('\n' * space_time)


# checking the value in the dictio
def spanish_func1():
    try:
        value_in_the_dictio = list(english_to_spanish.values())
        spanish_number = 'ocho'

        if spanish_number in value_in_the_dictio:
            print('yes the spanish number --', spanish_number, '-- is in the dictionary')
        else:
            print('no the spanish number --', spanish_number, '-- is not in the dictionary')

    except KeyError:
        print('not in dicto, please try again!')


def main():
    spanish_func0()
    spacing()
    spanish_func1()


main()
