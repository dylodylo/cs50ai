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
        print('--',i)
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.append((i,j))

    print(actions)
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        new_board = copy.deepcopy(board)
        #print(new_board)
        print("----")
        print(action[0],action[1])
        print(new_board[0][1])
        print(player(board))
        print("-----")
        new_board[action[0]][action[1]] = player(board)
        return new_board
        raise NameError
    except NameError:
        print("Error!")


    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in board:
        if i == ["X", "X", "X"]:
            return "X"
        elif i == ["O", "O", "O"]:
            return "O"
        elif board[0][0] == board[1][0] == board[2][0]:
            return board[0][0]
        elif board[0][1] == board[1][1] == board[2][1]:
            return board [0][1]
        elif board[0][2] == board[1][2] == board[2][2]:
            return board [0][2]
        elif board[0][0] == board[1][1] == board[2][2]:
            return board [0][0]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board [0][2]
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
        winner = winner(board)
        if winner == "X":
            return 1
        elif winner == "O":
            return -1
        else:
            return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    actions_ = actions(board)
    # for action in actions_:
    #     if winner(result(board, action)):
    #         pass
    
    
    return actions_[0]
    raise NotImplementedError
