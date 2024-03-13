def is_safe(board, row, col):
    return not any(board[i][col] or board[i][j] for i, j in zip(range(row, -1, -1), range(col, -1, -1))) and \
           not any(board[i][col] or board[i][j] for i, j in zip(range(row, 8), range(col, -1, -1))) and \
           not any(board[row][i] for i in range(col))
def solve_queens(board, col):
    if col >= 8: return True
    for i in range(8):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queens(board, col + 1): return True
            board[i][col] = 0
    return False
def place_queens():
    board = [[0] * 8 for _ in range(8)]
    print("Solution:" if solve_queens(board, 0) else "No solution exists")
    [print(*row) for row in board]
if __name__ == "__main__":
    place_queens()
