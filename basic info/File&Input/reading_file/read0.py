

#r - read, w-write, a-append , r+-read and write
user_file = open('employees.txt', 'r')

# make sure to have .readable() to check if you can even read the file
# print(user_file.read())
# print(user_file.readline())
# print(user_file.readlines())
#print(user_file.readlines()[2])

for user in user_file.readlines():
    print(user)


#always make sure to close the file
user_file.close()


