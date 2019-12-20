user_name = input("Enter your name: ")
password = input('What is the password: ')

user_login = str(user_name)
user_pass = str(password)

if user_name == 'Admin123' and password == 'password123$33':
    print('Welcome Admin')

else:
    print('Access is Denied')