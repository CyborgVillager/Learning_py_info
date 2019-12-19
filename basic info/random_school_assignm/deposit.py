#user choose
while True:
    user_choice = input('(Do you want to: A) see your future projetion?' + '\n' +
                    'or B)or see how much is required for a certain deposit goal? ')


    if user_choice in ['A','B']:
    # process the input 
        break

def future_projection():
    years = int(input('How long are you planning to deposit for? '))
    future = float(input('What is your desired profit for deposting for ' + str(years) + ' years? '))
    interest_rate = float(input('''''What is the bank's'''' interest rate? '))
    present_value = future // (1.0 + interest_rate) ** years
    present_deposit = int(input('How much are you planning to put in? '))
    deposit_profit = future // (1.0 + interest_rate) ** years

    if deposit_profit < future:
        print('Your profit is not high enough, its only', deposit_profit, 'for over', years,
              ' years','\n',' and not your designated future proejection goal of', future, 'dollars')
    else:
        print('Your profit is ', '$', deposit_profit, 'for over ', str(years), ' years')

def deposit_goal():
    years = int(input('How long are you planning to deposit for? '))
    future = float(input('What is your desired profit for deposting for ' + str(years) + ' years? '))
    interest_rate = float(input('''''What is the bank's'''' interest rate? '))
    present_value = future // (1.0 + interest_rate) ** years
    present_deposit = int(input('How much are you planning to put in? '))

    print('You will need to deposit this amount: ', present_value, ' dollars')


if user_choice == 'A':
    future_projection()

elif user_choice == "B":
    deposit_goal()


