"""
Tic Tac Toe Player
"""

import math
import copy

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
    emptys = 0
    for i in board:
        for j in i:
            if j == EMPTY:
                emptys += 1
    
    if emptys % 2 == 1:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.append((i,j))

    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise ValueError("Game over.")
    elif action not in actions(board):
        raise ValueError("Invalid action", action, board)
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
    
    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i == ["X", "X", "X"]:
            return X
        elif i == ["O", "O", "O"]:
            return O
    if board[0][0] == board[1][0] == board[2][0]!= None:
        if board[0][0] == "X":
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1]!= None:
        if board[0][1] == "X":
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2]!= None:
        if board[0][2] == "X":
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2]!= None:
        if board[0][0] == "X":
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0]!= None:
        if board[0][2] == "X":
            return X
        else:
            return O
    else:
        return None
            
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if not any(EMPTY in sublist for sublist in board):
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        winner_ = winner(board)
        if winner_ == X:
            return 1
        elif winner_ == O:
            return -1
        else:
            return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            max_v = minvalue(result(board,action))
            if max_v > v:
                v = max_v
                best_action = action
        
    elif player(board) == O:
        v = math.inf
        for action in actions(board):
            min_v = maxvalue(result(board,action))
            if min_v < v:
                v = min_v
                best_action = action
    
    return best_action


def maxvalue(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v


def minvalue(board):
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))

    return v