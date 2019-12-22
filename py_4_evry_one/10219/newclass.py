
class users:
    def __init__(self,user_names,first_name,last_name,gender):
        self.__user_names = user_names
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender

    def getUser_Names(self):
        return self.__user_names

    def getFirst_Name(self):
        return self.__first_name

    def getLast_Name(self):
        return self.__last_name

    def getGender(self):
        return self.__gender

def user_info():
    get_user = users('jon','joshua','almawi','male')
    print('the username is ' + get_user.getUser_Names() + '\n' +
          'the first name is ' + get_user.getFirst_Name() + '\n' +
          'the last name is ' + get_user.getLast_Name() + '\n' +
          get_user.getFirst_Name() + '\'s gender is ' + get_user.getGender())


def main():
    user_info()


main()