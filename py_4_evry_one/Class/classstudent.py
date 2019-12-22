class Student:
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


    def on_honor_roll(self):
        if self.gpa > 3.6:
            print(self.name, 'is on the honor roll list')
        else:
            print(self.name, 'is not on the honor roll list')