#key:val

student = {'name': 'John', 'age': 25, 'courses':['Math','CompSci']}


# to update the dictionary
student.update({'name':'Jame', 'age': 26, 'phone': '555-5555'})
#del student['age']
age = student.pop('age')
print(age)

#loop
print((len(student)))
print(student.keys())
print(student.values())
print(student.items())


# student['phone'] = '555-5555'
# student['name'] = 'Jane'

try:
    #dir_info0 = student['name']
    dir_info1 = student.get('name')
    student_find = dir_info1
    print(student_find)
    print(student)


except KeyError:
    print('The key does not exist')
