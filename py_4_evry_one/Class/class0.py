

class Patient():
    def __init__(self,first_name,last_name,id,age,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.age = age
        self.gender = gender


    def getfirst_name(self,first_name):
        return self.__first_name

    def getlast_name(self,last_name):
        return self.__last_name





def main():
    patient = Patient()
    print(patient.getfirst_name())


main()