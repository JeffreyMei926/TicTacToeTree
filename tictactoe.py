
# Import Libraries
import numpy as np

class search_tree:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.children = []
        self.utility = self.calculate_utility()

    def is_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.player or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] == self.player:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player:
            return True

        return False

    def is_loss(self):
        new_player = 'X' if self.player == 'O' else 'O'
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == new_player or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] == new_player:
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == new_player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == new_player:
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def calculate_utility(self):
        if self.is_win(): # win
            return 1
        elif self.is_loss():
            return -1
        elif self.is_board_full(): # draw
            return 0
        pass

    def generate_children(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    new_board = self.board.copy()
                    new_board[row][col] = self.player
                    new_player = 'O' if self.player == 'X' else 'X' # enemy token 
                    child = search_tree(new_board, new_player)
                    self.children.append(child)

    def print_board(self):
        print("-" * 9)
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)


def build_search_tree(board, player):
    root = search_tree(board, player)
    build_search_tree_recursive(root)
    return root

def build_search_tree_recursive(node):
    node.generate_children()
    for child in node.children:
        build_search_tree_recursive(child)

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

        if row > 3 or col > 3: 
            break

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
    # Find first empty 
    row, col = shallow_search_tree(board)
    return row, col

def find_empty_cell(board):
    for row in range(3):
        for col in range(3):

            if board[row][col] == '':
                return row,col

def shallow_search_tree(board):
    """
    - looks one step ahead
    - if loss imminent: prevent it
    - if win imminent: take it
    - else: take convenient choice
    """

    # Find Legal State
    for row in range(3):
        for col in range(3):

            if board[row][col] == '':
                next_board = board.copy()
                next_board[row][col] = 'X' # populate with enemy token

                # Prevent Loss
                if check_winner(next_board):
                    return row, col
    
    # if no winner, take first empty cell
    row, cell = find_empty_cell(board)
    return row, col

def evaluate_state(board, row, col, player):
    new_board = board.copy()
    new_board[row][col] = player

    if check_winner(new_board):
        return 1
    elif is_board_full(new_board):
        return 0
    else:
        evaluate_state(board) 

def is_terminal():
    '''
    evaluates position     
    '''

    if check_winner(board):
        return 1

    else if: is_board_full(board)
        return 0

def test_board(scenario):
    '''
    simple case to test search tree

    Parameter:
        scenario (int): number referening scenario 

    Return:
        board (array): scenario board
    '''

    board = np.array([[''] * 3] * 3)
    if scenario == 1:

        # Imminent Loss
        board[0][0] = 'X'; board[0][1] = 'X'; board[0][2] = ''; 
        board[1][0] = 'O'; board[1][1] = ''; board[1][2] = ''; 
        board[2][0] = ''; board[2][1] = ''; board[2][2] = '';

    elif scenario == 2:

        # Imminent Win
        board[0][0] = 'X'; board[0][1] = 'O'; board[0][2] = ''; 
        board[1][0] = 'X'; board[1][1] = ''; board[1][2] = ''; 
        board[2][0] = ''; board[2][1] = ''; board[2][2] = ''

    elif scenario == 3:

        # Imminent Win
        board[0][0] = 'X'; board[0][1] = 'O'; board[0][2] = ''; 
        board[1][0] = 'X'; board[1][1] = 'O'; board[1][2] = ''; 
        board[2][0] = ''; board[2][1] = ''; board[2][2] = ''


    elif scenario == 4:

        # Imminent Win
        board[0][0] = 'X'; board[0][1] = 'O'; board[0][2] = ''; 
        board[1][0] = 'X'; board[1][1] = 'O'; board[1][2] = ''; 
        board[2][0] = 'X'; board[2][1] = ''; board[2][2] = ''

    # Imminent Draw
    return board


if __name__ == "__main__":
    tic_tac_toe(one_player = True)


# ========
# Testing 
# ========
board = test_board(3)
player = 'X'
node = search_tree(board, player)
node.calculate_utility()

root = build_search_tree(board, player)
build_search_tree_recursive(node)


for child in root.children:
    if child.calculate_utility() is not None:
        print(child.calculate_utility())




