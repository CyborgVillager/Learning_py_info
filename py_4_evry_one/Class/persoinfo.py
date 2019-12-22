#will fix this, had to deal with an personal matter over the weekend
class Personal:
    def __init__(self,name,address,age,phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number


    def setName(self,name):
        self.name = name

    def setAddress(self,address):
        self.address = address

    def setAge(self,age):
        self.age = age

    def setPhone_Number(self,phone_number):
        self.phone_number = phone_number


    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhone_Number(self):
        return self.phone_number

    def toAquire_Personal_Data(self):
        return 'Your name is {} and your address is {} , your phone number is {} and lastly your age is {}  ' . \
            format(self.name,self.address,self.phone_number,self.age)

    '''
    def getFamilyInfo(self):
        self.name1 = 'Father'
        self.address1 = 'Elk Forest PArk etc etc'
        self.phone_number1 = '342452352'
        self.age1 = '55'



    def toAquire_Family_Info(self):
        return 'Your father name is {} his address is {}, his phone number is {}, and lastly his age is {}' .format(
            self.name1,self.address1,self.phone_number1,self.age1 )
'''




name = input('what is your name? ')
address = input('what is address? ')
age = int(input('How old are you? '))
phone_number = int(input('What is your phone number? '))


personal_info = Personal(name,address,age,phone_number)
print(personal_info.toAquire_Personal_Data())
#father1 = Personal('Father', 'Elgin Forest Pk', '8413413', '55')
#print(father1)





