#basic list

def basic_list():
    user_names = ['Lorem', 'lo', 'Vinny','kria','RT']
    user_names[1] = 'RT'

    user_input = input('Enter a new name: ')
    user_names.append(user_input)
    age = [15 , 17 , 18 ,16]

    print(user_names[2])
    print(user_names[-2])
    print(user_names[1:3])
    print(user_names)
    print(age[1])


    #check if an info is in a list
    print(user_names.index('RT'))
    print('RT shows up ' + str(user_names.count('RT')) + ' times ')

def main0():
    basic_list()


main0()


