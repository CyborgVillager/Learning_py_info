#one acre of land is equivalent to 43 560 sq ft.
#ask user to enter ttl square feet 4 the land
#calc user inputted # of acres then divide it by  43 560k to get the acre

#default number for an acre of land
acre_of_land = 43560

#ask the buyer how many of sq. feet they would like to buy
ask_user_for_square_feet = int(input('How many of square feet would you' + '\n'
                                       + 'like to purchase today? '))

#calculate user input and divide it by the acre of land
calc_user_input_with_acre_of_land = (ask_user_for_square_feet / acre_of_land)

#print out statement for the buyer and round of the # of
#acres that they are buying it
print('You are purchasing over ' + str(round(calc_user_input_with_acre_of_land)) +
      ' acres of land')

#End of Program
#Made by Jonathan Almawi
