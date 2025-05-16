N = 5  # Size of the chessboard (5x5)

# Function to print the board
def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")  
        print()  

# Function to check if it's safe to place a queen
def is_safe(board, row, col):
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# Function to solve the N-Queen problem using backtracking
def solve(board, col):
    if col >= N:
        return True  # All queens are placed successfully

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1  
            if solve(board, col + 1):  
                return True
            board[i][col] = 0  

    return False 

# Initialize the chessboard with all 0s (empty spaces)
board = [[0 for _ in range(N)] for _ in range(N)]

# Start solving the N-Queen problem
if solve(board, 0):
    print("Solution for 5 Queens:")
    print_board(board)
else:
    print("No solution found.")