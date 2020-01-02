from text_color import *
# tutorial from CS Dojo -> https://www.youtube.com/watch?v=wfcWRAxRVBA
# made some improvements for Pt1, will check PT2 and update if nessa.

'''''
Old Code
# Robot Color Codes, Change as needed
robot0_color_code = red
'''''


class Robot:
    def __init__(self,givenName,givenColor,process_Speed):
        self.name = givenName
        self.color = givenColor
        self.processing_speed_percent = process_Speed

    def introduct_self(self):
        print('Hello my A.I\'s name is ' + yellow + self.name + end + ' , their main color is ' +
              self.color + end + ' and it\'s processing speed is ' + yellow +
              str(self.processing_speed_percent) + end + '%')

'''''
Old Code
# Robot0
robot0 = Robot()
robot0.name = 'John'
robot0.color = 'red'
robot0.color_show = colors['RED']
robot0.process_speed_percent = 25

# Robot1
robot1 = Robot()
robot1.name = 'Josh'
robot1.color = 'green'
robot1.color_show = colors['GREEN']
robot1.process_speed_percent = 35
'''''

user_input_name = input('Type your A.i\'s name: ' )
user_input_color = input('What is ' + user_input_name + '\'s color? ').lower()

if user_input_color == 'red':
    user_input_color = red + 'red'
elif user_input_color == 'purple':
    user_input_color = purple + 'purple'
elif user_input_color == 'cyan':
    user_input_color = cyan + 'cyan'
elif user_input_color == 'blue':
    user_input_color = blue + 'blue'
elif user_input_color == 'green':
    user_input_color = green + 'green'
elif user_input_color == 'yellow':
    user_input_color = yellow + 'yellow'
elif user_input_color == 'dark cyan' or user_input_color == 'darkcyan' or user_input_color == 'dark_cyan':
    user_input_color = dark_cyan + 'dark cyan'
else:
    user_input_color = unknown_color

while True:
    try:
        user_input_process_speed = int(input('What is '+ user_input_name +'\'s processing speed? '))
        break
    except ValueError:
        print('\n ')
        print('Type an integer for ' + user_input_name +'\'s speed ')


robot0 = Robot(user_input_name, user_input_color,user_input_process_speed)
# robot1 = Robot('Josh','blue',44)



robot0.introduct_self()
#robot1.introduct_self()