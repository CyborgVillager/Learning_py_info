#while true statement/ see if user choose to see/add their balence or to see
#their login information
while True:
    bank_info = input('If you want to see your bank balance type: A)'+ '\n'
                      + 'else to see your bank login info type: B) ')
    if bank_info in ['A', 'B']:

        break

#functions
def bank_bal():
    deposit = int(input('how much would you like to deposit?'))
    current_balance = int(input('How much do you have now?'))
    total = current_balance + deposit
    print('Your total balance is $' + str(total))
def login_info():
    user_name = input('What is your username?')
    password = input('What is your password?')
    print('Your username is' + user_name, 'and your password is ' + password)

#result if user choose option A or B
if bank_info == 'A':
    bank_bal()
elif bank_info == 'B':
    login_info()