file = 'maze1.txt'
text = open(file, 'r')
board = []
board_rows = len(open(file).readlines()) - 3
start_point = 0
goal_point = 0


def setup():

    for i in range(board_rows):
        wall_place = text.readline().split(', ')
        wall_place[-1] = wall_place[-1][0]
        board.append(wall_place)

    useless_ = text.readline()
    start_point = text.readline().replace("\n", "")

    goal_point = text.readline().replace("\n", "")

    for a in board:
        print(*a)

    print("------------------------------------------")

    print(start_point)

    print(goal_point)



setup()
