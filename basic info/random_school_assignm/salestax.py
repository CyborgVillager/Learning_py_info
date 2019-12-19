#Ask the user on what product they would like to list their
#product for and how much they are selling it for
#by listing it on our site
ask_user_for_merchandise = input('Please enter customer merchandise name: ')
ask_user_for_purchase = float(input('What is the amount of purchase, for '
                                   + ask_user_for_merchandise + '\n'
                                   'the customer would like to list it for?: '))

#How much of an amount of purchase the customer has to buy from our user
#After obtaining our user's merchandise name, change var to merchandise name
#for better continuity
merchandise_name = ask_user_for_merchandise
amount_of_purchase = ask_user_for_purchase

#inputing taxes from both state and county,
#including the combined tax
#and total bill
county_tax = .025 * amount_of_purchase
state_tax = .05 * amount_of_purchase
combined_tax = state_tax + county_tax
total_bill = combined_tax + amount_of_purchase

#tell user county and state taxes are included
#print out results for State,County,Combined Taxes, and
#the total bill for the customer
#all results are rounded for better readability for the user
print('')
print('County and state taxes are included for ', merchandise_name)
print('County tax is: $', round(county_tax))
print('State tax is: $', round(state_tax))
print('Combined tax is: $',round(combined_tax))
print('Total Bill is: $', round(total_bill))

#End of Program
#Made by Jonathan Almawi
#<(^_^)>

