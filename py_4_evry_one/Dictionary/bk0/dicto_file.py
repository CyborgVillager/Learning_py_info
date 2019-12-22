
def reading_break_line():
    file_name = input('Enter the filename: ')
    try:
        file_name = open(file_name)
    except FileNotFoundError:
        print('The file', file_name,  'doesn\'t exist, please try again! ')
        exit()

    counting = dict()
    for line in file_name:
        words = line.split()
        for word in words:
            if word not in counting:
                counting[word] = 1
            else:
                counting[word] += 1
    print(counting)



def main():
    reading_break_line()


main()