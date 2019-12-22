import threading
import random
import os
import time

# special thanks to Engineer Man for the Tutorial :
# https://www.youtube.com/watch?v=lbbNoCFSBV4&list=PLlcnQQJK8SUj5vlKibv8_i42nwmxDUOFc&index=7

def tree():
    # mutex

    mutex = threading.Lock()
    tree = list(open('tree1.txt').read().rstrip())

    def colored_dot(color):
            if color == 'red':
                return f'\033[91m⏺\033[0m'
            if color == 'green':
                return f'\033[92m⏺\033[0m'
            if color == 'yellow':
                return f'\033[93m☆\033[0m'
            if color == 'blue':
                return f'\033[94m⏺\033[0m'
    # threading the lights
    def lights(color, indexes):
        off = True
        while True:
            for index in indexes:
                tree[index] = colored_dot(color) if off else '⏺'
            # ensure the 'tree' wont go on top of each other, more of ease of transition
            mutex.acquire()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(''.join(tree))
            mutex.release()
            off = not off

            time.sleep(random.uniform(.5,1.5))




    yellow = []
    red = []
    green = []
    blue = []
    bulb_yellow = 'Y'
    bulb_red = 'R'
    bulb_green = 'G'
    bulb_blue= 'B'

# https://www.geeksforgeeks.org/enumerate-in-python/
    for index, characters in enumerate(tree):
        if characters == bulb_yellow:
            yellow.append(index)
            tree[index] = '☆'
        if characters == bulb_red:
            red.append(index)
            tree[index] = '⏺'
        if characters == bulb_green:
            green.append(index)
            tree[index] = '⏺'
        if characters == bulb_blue:
            blue.append(index)
            tree[index] = '⏺'

    thread_yellow = threading.Thread(target=lights, args=('yellow', yellow))
    thread_red = threading.Thread(target=lights, args=('red', red))
    thread_green = threading.Thread(target=lights, args=('green', green))
    thread_blue = threading.Thread(target=lights, args=('blue', blue))
    # start all 4 bulb's & join them

    for electric_thread in [thread_yellow,thread_red,thread_green,thread_blue]:
        electric_thread.start()
    for electric_thread in [thread_yellow, thread_red, thread_green, thread_blue]:
        electric_thread.join()
#    print(''.join(tree), yellow,red,green,blue)


def main():
    tree()


main()