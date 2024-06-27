import random
import time

def create_board():
    """
    This function creates the game board for Tic-Tac-Toe.
    It initializes the board with empty spaces represented by '-'
    """
    board = [["-" for _ in range(3)] for _ in range(3)]
    return board


def display_board(board):
    """
    This function takes in the current game board and displays it to the players
    """
    print("-------------")
    for row in board:
        print("|", end="")
        for element in row:
            print(f" {element} |", end="")
        print("\n-------------")


def user_input(board):
    """
    This function takes in the current game board and prompts the user to input their desired row and column to place their symbol
    """
    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            if board[row][col] == "-":
                board[row][col] = 'X'
                return board
            else:
                print("This cell is already filled. Please choose another cell.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
        except IndexError:
            print("Invalid input. Please enter a number between 1 and 3.")


def minimax(board, depth, is_max):
    if check_win(board) == 'X':
        return -1
    elif check_win(board) == 'O':
        return 1
    elif check_tie(board):
        return 0

    if is_max:
        max_eval = float('-inf') # COMPUTER
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, not is_max)
                    board[i][j] = "-"
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf') # PLAYER
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, not is_max)
                    board[i][j] = "-"
                    min_eval = min(min_eval, eval)
        return min_eval


def computer_input(board):
    print("Computer is thinking...")
    best_eval = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = 'O'
                eval = minimax(board, 0, False) # EVAL OF PREVIOUS PLAYER STEP
                board[i][j] = "-"
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = 'O'
    return board


def check_win(board):
    """
    This function checks if there is a winning combination of symbols on the board
    """
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return board[i][0]
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]
    return None


def check_tie(board):
    """
    This function checks if the game is a tie
    """
    return all(all(cell != '-' for cell in row) for row in board)


# Create the board
board = create_board()

# Game Loop
while True:
    display_board(board)

    # Player's turn
    board = user_input(board)
    display_board(board)
    if check_win(board) == 'X':
        print("You win!")
        break
    elif check_tie(board):
        print("It's a tie!")
        break

    # Computer's turn
    board = computer_input(board)
    if check_win(board) == 'O':
        display_board(board)
        print("Computer wins!")
        break
    elif check_tie(board):
        display_board(board)
        print("It's a tie!")
        break