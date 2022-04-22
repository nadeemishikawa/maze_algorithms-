import random

file = 'minesweeper1.txt'
text = open(file, 'r')
board_rows = len(open(file).readlines())

uv_board = []
v_board = []
unknown_list = []
board_cols = 0
mine_number = 0
hidden_number = 0


def setup():
    # read text file and convert into board(Two-dimensional array)
    for i in range(board_rows):
        bomb_place = text.readline().split()
        uv_board.append(bomb_place)

    board_cols = len(uv_board[0])
    
    # make visible board(Two-dimensional array)
    for i in range(board_rows):
        sublist = []
        for j in range(board_cols):
            sublist.append("*")
        v_board.append(sublist)



    # make unknown board(list)
    for i in range(board_rows):
        for j in range(board_cols):
            unknown_list.append(f"{i}{j}")

    mine_number = sum(x.count('M') for x in uv_board)
    hidden_number = len(unknown_list)



# update visible board
def reboard(row, col):
    if row < 0 or col < 0 or col > board_cols - 1 or row > board_rows - 1 or v_board[row][col] != "*":
        pass
    elif uv_board[row][col] == "M":
        print("testttttttttttttttttttttttttttttttttttttt")
        return True

    elif uv_board[row][col] == "0":
        v_board[row][col] = uv_board[row][col]

        # Recursive
        reboard(row + 1, col)  # right
        reboard(row, col + 1)  # up
        reboard(row, col - 1)  # down
        reboard(row - 1, col)  # left
        reboard(row + 1, col + 1)  # 右上
        reboard(row + 1, col - 1)  # hidari 上
        reboard(row - 1, col + 1)  # 右上
        reboard(row - 1, col - 1)
    else:
        v_board[row][col] = uv_board[row][col]


def play_ai_move():

    pass


def show_board():
    for a in v_board:
        print(*a)
    print("------------------------------------------")


def judge():
    mine_number = sum(x.count('M') for x in uv_board)
    hidden_number = len(unknown_list)
    uncover = hidden_number - mine_number
    return uncover is not 0


def play():
    while judge():
        col = int(input(f"Please input a number(1 to {board_cols}) as col (ex.{board_cols}):")) - 1
        row = int(input(f"Please input a number(1 to {board_rows}) as row (ex.{board_rows}):")) - 1

        it_is_bomb = reboard(row, col)
        if it_is_bomb:
            print("game over")
            break
        show_board()


def clear():
    if not judge():
        print("congratulations!!")


def main():
    setup()
    show_board()
    play()
    clear()


if __name__ == '__main__':
    main()
