"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_of_x = 0
    num_of_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                num_of_x += 1
            elif board[i][j] == "O":
                num_of_o += 1

    if num_of_x == num_of_o:
        return "X"
    else:
        return "O"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_of_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                set_of_actions.add((i, j))
    
    return set_of_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tmp_board = board

    turn = player(board)
    tmp_board[action[0]][action[1]] = turn
    return tmp_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] and board[0][1] == board[1][1]:
        return board[0][1]
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][0]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                cnt += 1
    
    if cnt == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

def find_max(board):
    if terminal(board):
        return utility(board)

    best = -(2 ** 32)

    for action in actions(board):
        res = find_min(result(board, action))

        best = max(res, best)
    
    return best

def find_min(board):
    if terminal(board):
        return utility(board)

    best = 2 ** 32

    for action in actions(board):
        res = find_max(result(board, action))

        best = min(best, res)

    return best

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    x = -1
    y = -1

    if player(board) == "X":
        best = -(2 ** 32)

        for action in actions(board):
            v = find_max(result(board, action))

            if best < v:
                x = action[0]
                y = action[1]
                best = find_max(result(board, action))

    else:
        best = (2 ** 32)

        for action in actions(board):
            v = find_min((result(board, action)))

            if best > v:
                x = action[0]
                y = action[1]
                best = v

    return (x, y)
