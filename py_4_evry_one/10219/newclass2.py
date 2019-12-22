

class User():

        def __init__(self,username,first_name,last_name):
            self.__username = username
            self.__first_name = first_name
            self.__last_name = last_name

        def getUserName(self):
            return self.__username
        def getFirstName(self):
            return self.__first_name
        def getLastName(self):
            return self.__last_name


def class_info():
    wow = User('joshua2000','josh','almawi')
    print(wow.getFirstName(),wow.getLastName(), ' user name is ' , wow.getUserName())


def main():
    class_info()


main()