# Write a function 'convertFTOc' that takes 1 paremeter
# degree in F in the func, and convert F to C
# return C degree to the caller
# Follow this formula C = (F - 32) * 5/9

# main function that ask user to input F degree, calls
# convertFtoC, func and print out C on
# the screen
# Result - call main()
#This is global already called for covnertFtoC():

tell_user_of_information = float(input('Please enter Fahrenheit to calculate the' + '\n' +
                                  'C = (F- 32) * 5/9' + 'C is Celius: '))
#ask_user_for_fahrenheit = float(input('Fahrenheit : '))

#converting the information from the user input
def convertFtoC():
 #   user_info = tell_user_of_information its already being called , since its global
    converting = (tell_user_of_information - 32) * 5/9
    celsius = converting
    print('the celsius is' , round(celsius), '°c')

#main function
def main():
    convertFtoC()
    # ask_user = ask_user_for_fahrenheit
    input('Please press enter to quit program, thank you')
    input('Goodbye!')

#result
main()