from random import randint


def player_input():
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to be X or O? ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def choose_first():
    if randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def display_board(board):
    for ridx, row in enumerate(board):
        print(" ")
        for cidx, el in enumerate(row):
            if cidx != len(row) - 1:
                print(el + " | ", end="")
            else:
                print(el)
        if ridx != len(board) - 1:
            print("----------")


def space_check(board, row, col):
    return board[row][col] == " "


def player_choice(board):
    row = -1
    col = -1
    while (row not in range(0, 3) and col not in range(0, 3)) or not space_check(
        board, row, col
    ):
        row, col = map(int, input("Choose your next position [0-2][0-2]: ").split())
    return row, col


def place_marker(board, marker, row, col):
    board[row][col] = marker


def win_check(board, mark):
    # Check rows
    for row in board:
        if row[0] == mark and all(el == row[0] for el in row):
            return True
    # Check columns
    for col in zip(*board):
        if col[0] == mark and all(el == col[0] for el in col):
            return True
    # Check diagonals
    if board[1][1] == mark:
        if (board[1][1] == board[0][0] == board[2][2]) or (
            board[1][1] == board[0][2] == board[2][0]
        ):
            return True
    return False


def full_board_check(board):
    for row in range(0, 3):
        for col in range(0, 3):
            if space_check(board, row, col):
                return False
    return True


def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")


if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    while True:
        the_board = [[" "] * 3 for _ in range(0, 3)]
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + " will go first.")

        play_game = input("Are you ready to play? Enter Yes or No: ")

        if play_game.lower()[0] == "y":
            game_on = True
        else:
            game_on = False
        while game_on:
            if turn == "Player 1":
                display_board(the_board)
                row, col = player_choice(the_board)
                place_marker(the_board, player1_marker, row, col)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print("Congratulations! You have won the game!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = "Player 2"
            else:
                display_board(the_board)
                row, col = player_choice(the_board)
                place_marker(the_board, player2_marker, row, col)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print("Player 2 has won!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = "Player 1"
        if not replay():
            break
