# learning on how to make a snake game / user controls / etc
# thanks in part to Engineer Man -> https://www.youtube.com/watch?v=rbasThWVb-c&t=85s
# Engineer Man Python Playlist -> https://www.youtube.com/watch?v=lbbNoCFSBV4&list=PLlcnQQJK8SUj5vlKibv8_i42nwmxDUOFc&index=7
# make sure to install curses via terminal -> pip install windows-curses
#to start the game use cmd or cmder access the folder and type either python snake.py or tree_electric_code.py
import random
import curses




initlize = curses.initscr()
curses.curs_set(0)

screen_height,screen_width = initlize.getmaxyx()

window = curses.newwin(screen_height,screen_width, 0, 0)
window.keypad(1)
#refresh every mili-second
window.timeout(100)

snake_xposition = screen_width/4
snake_yposition = screen_height/2

snake = [
    #body part of the snake
    # diagram of the snake [][][]
    [snake_yposition, snake_xposition],
    [snake_yposition, snake_xposition-1],
    [snake_yposition, snake_xposition-2],
]

food = [screen_height/2, screen_width/2]
window.addch(int(food[0]), int(food[1]), curses.ACS_LANTERN)

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0,screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
        import image
        image()
        quit()

    new_snake_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_snake_head[0] += 1
    if key == curses.KEY_UP:
        new_snake_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_snake_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_snake_head[1] += 1

    snake.insert(0,new_snake_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1,screen_height-1),
                random.randint(1,screen_width-1)

            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0],food[1], curses.ACS_LANTERN)
    else:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')

    window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)