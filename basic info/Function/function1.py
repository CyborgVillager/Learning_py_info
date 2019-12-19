user_name = input('Please enter your name: ')
user_age = int(input("Please enter your age: "))


def ask_user(user_name,user_age):

    print('Hello ' + user_name + ' your age is: ' + str(user_age))


def main():
    ask_user(user_name, user_age)

main()

 