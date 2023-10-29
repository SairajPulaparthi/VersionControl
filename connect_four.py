#SairajPulaparthi
#10/11/2023
#connectfourgame


#the def to start the board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()
#this is in charge of the number of rows and number of columns that it needs.
def initialize_board(num_rows, num_cols):
    result = []
    for i in range(num_rows):
        row = []
        for i in range(num_cols):
            row.append("-")
        result.append(row)

    return result




#this is where the process of inserting each chip would occur
def insert_chip(board, col, chip_type):

    for num_row in reversed(board):

        if num_row[col] == "-":
            num_row[col] = chip_type
            return num_row
#this is when the token is added it would see if the location is valid or a connct four has occured winning the game.
def check_if_winner(board, col, row, chip_type):

    area = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for Ar, Ac in area:
        keep = 0

        for i in range(-3, 4):
            numRow, numCol = row + i * Ar, col + i * Ac
            if 0 <= numRow < len(board) and 0 <= numCol < len(board[0]) and board[numRow][numCol] == chip_type:
                keep += 1
                if keep == 4:
                    return True
    return False
#main function here call the other functions into.
def main():


    print("What would you like the height of the board to be?")
    number_row = int(input())
    print("What would you like the length of the board to be?")
    number_col = int(input())

    board = initialize_board(number_row, number_col)
    print_board(board)
    print("Player 1: x")
    print("Player 2: o")


    users = ['o', 'x']
    user_names = ["Player 2", "Player 1"]

    for i in range(1, number_row * number_col + 1):
        player = i % 2

        print(f"{user_names[player]}: Which column would you like to choose?")

        pick_col = int(input())

        for each_row in reversed(board):
            if each_row[pick_col] == "-":
                each_row[pick_col] = users[player]

                break

        print_board(board)

        if check_if_winner(board, pick_col, board.index(each_row), users[player]):
            print(f"{user_names[player]} won the game!")

            break
    else:

        print("Draw. Nobody wins.")



if __name__ == "__main__":
    main()


