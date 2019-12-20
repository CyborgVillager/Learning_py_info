
# immiditate convert
numb0 = float(input('Enter your first number: '))

# Operator
op = input('Enter operator: ')
#second number
numb1 = float(input('Enter your second number: '))

# if staterment

if op == '+':
    print(numb0 + numb1)

elif op == '-':
    print(numb0 - numb1)

elif op == '%':
    print(numb0 % numb1)

elif op == '*':
    print(numb0 * numb1)

elif op == '/':
    print(numb0 / numb1)

else:
    print('Please choose a mathematical operation such as +, -, /, or %' + '\n' +
          'Thank you...')
