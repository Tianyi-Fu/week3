import random
import sys

list_merge = [0, 0, 0, 0]


def zero_to_end():
    for x in range(len(list_merge) - 1, -1, -1):
        if list_merge[x] == 0:
            del list_merge[x]
            list_merge.append(0)


def merge():
    zero_to_end()
    for x in range(len(list_merge) - 1):
        if list_merge[x] == list_merge[x + 1]:
            list_merge[x] *= 2
            del list_merge[x + 1]
            list_merge.append(0)


map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]


def move_left():
    global list_merge
    for line in map:
        list_merge = line
        merge()


def move_right():
    global list_merge
    for line in map:
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge


def square_matrix_transposition():
    for x in range(1, len(map)):
        for y in range(x, len(map)):
            map[y][x - 1], map[x - 1][y] = map[x - 1][y], map[y][x - 1]


def move_up():
    square_matrix_transposition()
    move_left()
    square_matrix_transposition()


def move_down():
    square_matrix_transposition()
    move_right()
    square_matrix_transposition()


def add():
    d = {}
    a = 0
    for x in range(4):
        for y in range(4):
            if not map[x][y]:
                d[a] = (x, y)
                a += 1
    if a == 0:
        print("You lose")
        sys.exit()
    num_add = random.choice([4, 2, 2, 2])
    num_index = random.randint(0, a - 1)
    map[d[num_index][0]][d[num_index][1]] = num_add
    return map


def draw_map():
    for x in map:
        for y in x:
            print(y, end="\t")
        print()


def move_map():
    do = input("Enter to move(w:up s:down a:left d:right e:exit):")
    if do == "w":
        move_up()
    elif do == "s":
        move_down()
    elif do == "a":
        move_left()
    elif do == "d":
        move_right()
    elif do == "e":
        sys.exit()
    else:
        print("Please enter again")


def update():
    while True:
        move_map()
        add()
        draw_map()


def main():
    draw_map()
    update()


main()
