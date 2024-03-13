import math
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1
BOARD_SIZE = 3
WIN_SCORE = 1
DRAW_SCORE = 0
LOSE_SCORE = -1
def evaluate(board):
    """
    Evaluate the current state of the board.
    """
    for row in board:
        if sum(row) == BOARD_SIZE:
            return WIN_SCORE
        elif sum(row) == -BOARD_SIZE:
            return LOSE_SCORE
    for col in range(BOARD_SIZE):
        if sum(board[row][col] for row in range(BOARD_SIZE)) == BOARD_SIZE:
            return WIN_SCORE
        elif sum(board[row][col] for row in range(BOARD_SIZE)) == -BOARD_SIZE:
            return LOSE_SCORE
    if sum(board[i][i] for i in range(BOARD_SIZE)) == BOARD_SIZE:
        return WIN_SCORE
    elif sum(board[i][i] for i in range(BOARD_SIZE)) == -BOARD_SIZE:
        return LOSE_SCORE
    if sum(board[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)) == BOARD_SIZE:
        return WIN_SCORE
    elif sum(board[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)) == -BOARD_SIZE:
        return LOSE_SCORE
    return DRAW_SCORE
def alpha_beta(board, depth, alpha, beta, is_maximizing):
    """
    Implementation of the Alpha-Beta Pruning algorithm.
    """
    score = evaluate(board)
    if score != DRAW_SCORE:
        return score
    if is_maximizing:
        best_score = -math.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    score = alpha_beta(board, depth + 1, alpha, beta, False)
                    board[row][col] = EMPTY
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    score = alpha_beta(board, depth + 1, alpha, beta, True)
                    board[row][col] = EMPTY
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score
def find_best_move(board):
    """
    Find the best move for the current player using Alpha-Beta Pruning.
    """
    best_score = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                score = alpha_beta(board, 0, alpha, beta, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move
if __name__ == "__main__":
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    board[0][0] = PLAYER_O
    board[1][1] = PLAYER_X
    board[2][2] = PLAYER_O
    print("Current Board:")
    for row in board:
        print(row)
    best_move = find_best_move(board)
    print("Best Move for Player X:", best_move)
