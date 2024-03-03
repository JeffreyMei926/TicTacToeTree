
# Import Libraries
import numpy as np

def print_board(board):
    print("-" * 9)
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """
    Parameters: 
        board (array):

    Returns:
        bool: flag to determine if there is a winner
    """

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '' or \
           board[0][i] == board[1][i] == board[2][i] != '':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '' or \
       board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False

def is_board_full(board):
    """
    Parameters:
        board (array): board indicating game state

    Returns:
    """

    for row in board:
        if '' in row:
            return False
    return True

def tic_tac_toe_2player():

    board = np.array([[''] * 3] * 3)
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == '':
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")
        

def tic_tac_toe_1player():

    board = np.array([[''] * 3] * 3)

    while True:
        print_board(board)

        current_player = 'X'
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == '':
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player= 'O'
                row, col = get_response(board)
                board[row][col] = current_player
        else:
            print("Cell already taken. Try again.")


def tic_tac_toe(one_player=True):
    """
    Runs tic-tac-toe game 

    Parameters:
        one_player (bool): flag for play against AI or not
    """
    if one_player is True:
        tic_tac_toe_1player()
    else:
        tic_tac_toe_2player()

    

def get_response(board):
    """
    finds MCST response to given state 
    """
    # Find first 
    for row in range(3):
        for col in range(3):
            if board[row][col] == '': 
                return row, col


if __name__ == "__main__":
    tic_tac_toe(one_player = True)




