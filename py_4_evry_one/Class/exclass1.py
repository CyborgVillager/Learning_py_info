#class features
#methods, initilizaiton, and help text
import datetime

class User:
    #to get help string use ''' or """ three time and place ur info
    """
    A member of Your fam. For now only sotring their bnames and birthday, and
    other info for them
    """
    #init = initialization, aka Constructor
    def __init__(self,full_name,birthday):
        self.name = full_name
        #this stores the val       value provided for user obj
        self.birthday = birthday  #yearmonthday format

        #Exteract first and last name
        name_pieces = full_name.split(' ')
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]



#user = User(full_name, birthday)
user = User('Jonathan Al', 1091997)

#print(user.name)
#print(user.birthday)
print(user.first_name)
print(user.last_name)
print(user.birthday)

#to get help info use
help(User)