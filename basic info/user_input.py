
def user_input_info():
    get_name = input("Type your name: ")
    get_age = int(input("Enter your age: "))
    sent = (' is age : ')

    print(get_name + sent +  str(get_age))


def main():
    user_input_info()


main()