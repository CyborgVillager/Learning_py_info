

try:
    ans = 10/0
    number = int(input('Enter a number: '))
    print(number)

# https://docs.python.org/3/tutorial/errors.html
# learn more on specific errors+
except ZeroDivisionError as zero_error:
    print(zero_error)

except ValueError:
    print('Invalid Input')