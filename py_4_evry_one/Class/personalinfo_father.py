class Personal:
    def __init__(self,name,address,age,phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number


def getFamilyInfo(self):
    self.name1 = 'Father'
    self.address1 = 'Elk Forest PArk etc etc'
    self.phone_number1 = '342452352'
    self.age1 = '55'


def toAquire_Family_Info(self):
    return 'Your father name is {} his address is {}, his phone number is {}, and lastly his age is {}'.format(
        self.name1, self.address1, self.phone_number1, self.age1)



personal_info = Personal(name,address,age,phone_number)
print(personal_info.toAquire_Family_Info())
