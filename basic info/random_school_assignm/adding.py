#1  2 3 4 5


numbers = [1, 2, 5]

count = 0

for number in '1 2 3 5'.split():
    count = count + int(number)
print(count)