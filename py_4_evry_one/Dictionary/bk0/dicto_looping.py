counts = { 'chuck': 1, 'annie': 42, 'jan': 100}

def v0():
    for key in counts:
        print(key,counts[key])
        #loops the info for each key in their respective value

def v1():
    for key in counts:
        if counts[key] > 10 :
            print(key, counts[key])

def spacing():
    space_times = 1
    times = '\n' * space_times
    dotted_line = ' -----' + times + ' -----'
    print(dotted_line)

def main():
    v0()
    spacing()
    v1()

main()
