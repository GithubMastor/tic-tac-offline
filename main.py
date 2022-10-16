from colorama import Fore

board = []

def make_board():
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)


def prnt_board(board):
    x = 0
    for row in board:
        y = 0
        for item in row:
            if y < 2:
                print(Fore.RESET + f'{item} |', end= ' ')
                y+=1
            else: print(f'{item}', end=' ')
        print()
        if x < 2:
            print('----------')
            x+=1


def player_win(board):
    n = len(board)
    #horiz
    for x in range(n):
        check_x = 0
        check_o = 0
        for y in range(3):
            if board[x][y] == 'X':
                check_x+=1
                if check_x==3:
                    return True
            if board[x][y] == 'O':
                check_o+=1
                if check_o==3:
                    return True
            else:
                continue

    #vert
    for x in range(n):
        check_x = 0
        check_o = 0
        for y in range(3):
            if board[y][x] == 'X':
                check_x+=1
                if check_x==3:
                    return True
            if board[y][x] == 'O':
                check_o += 1
                if check_o == 3:
                    return True

            else:
                continue

    #diag
    if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        return True
    if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        return True

    return False


def check_avail(board, row, column):
    if board[row][column] == 'X' or board[row][column] == 'O':
        return False
    else:
        return True


def set_position(board, player,row,column):
    board[row][column] = player

def change_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'











def start_game():
    player = 'O'
    make_board()
    player_win(board)
    while player_win(board) == False:
        player = change_player(player)

        prnt_board(board)
        if player == 'X':
            print(Fore.YELLOW +  f"\n------------------\nPlayer {player}'s turn")
        else:
            print(Fore.BLUE + f"\n\nPlayer {player}'s turn")

        if player == 'X':
            while True:
                while True:
                    row = input(Fore.YELLOW +  "Enter row number (0-2): ")
                    if row.isnumeric():
                        row = int(row)
                        if row < 3:
                            break
                    else:
                        continue
                while True:
                    column = input(Fore.YELLOW +  "Enter column number (0-2): ")
                    if column.isnumeric():
                        column = int(column)
                        if column < 3:
                            break
                    else:
                        continue
                if check_avail(board,row,column):
                    set_position(board,player,row,column)
                    break
                else:
                    print(Fore.RED + "That Position is Taken\nPlease Choose a New Position")
                    continue

        else:
            while True:
                while True:
                    row = input(Fore.BLUE + "Enter row number (0-2): ")
                    if row.isnumeric():
                        row = int(row)
                        if row < 3:
                            break
                    else:
                        continue
                while True:
                    column = input(Fore.BLUE + "Enter column number (0-2): ")
                    if column.isnumeric():
                        column = int(column)
                        if column < 3:
                            break
                    else:
                        continue
                if check_avail(board,row,column):
                    set_position(board, player, row, column)
                    break
                else:
                    print(Fore.RED + "That Position is Taken\nPlease Choose a New Position")
                    continue



    print(Fore.GREEN + '\n---------------\n')
    prnt_board(board)
    print(Fore.GREEN + f'\n---------------\nPlayer {player} WINS\n---------------')




if __name__ == '__main__':
    start_game()

