secret_word = 'learning'
user_guess = ' '
guess_count = 0
guess_limit = 3
guess_minus = 3
out_of_guess = False

#while loop
while user_guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        print('You currently have ' + str(guess_minus) + ' tries before being locked out' )
        user_guess = input('Enter authorized word to enter: ')
        guess_count += 1
        guess_minus -= 1
    else:
        out_of_guess = True

if out_of_guess:
    print('Sorry you have maxed out on incorrect login attempts')
else:
    print('Authorized granted..')
