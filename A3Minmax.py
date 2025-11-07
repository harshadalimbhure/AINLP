#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx
import math  # Import math for infinity values

# Function to print the board neatly
def print_b(b):
    [print(" | ".join(r)) for r in b]  # Print each row separated by '|'
    print()  # Blank line for readability

# Function to check if any moves are left
def mv_left(b):
    return any(c == ' ' for r in b for c in r)  # True if any empty cell exists

# Function to evaluate the board and return a score
def val(b):
    # Check rows for win
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != " ":
            return 10 if b[i][0] == "X" else -10
        # Check columns for win
        if b[0][i] == b[1][i] == b[2][i] != " ":
            return 10 if b[0][i] == "X" else -10

    # Check diagonals for win
    if b[0][0] == b[1][1] == b[2][2] != " ":
        return 10 if b[0][0] == "X" else -10
    if b[0][2] == b[1][1] == b[2][0] != " ":
        return 10 if b[0][2] == "X" else -10

    return 0  # No winner yet

# Minimax function to find the best score recursively
def mini(b, ismax):
    s = val(b)  # Evaluate board
    if s or not mv_left(b):  # Base case: win, lose, or draw
        return s

    # If maximizing player (AI = X)
    best = -math.inf if ismax else math.inf

    # Try all possible moves
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'X' if ismax else 'O'  # Make move
                # Recursive call for opponent
                best = max(best, mini(b, not ismax)) if ismax else min(best, mini(b, not ismax))
                b[i][j] = ' '  # Undo move (backtrack)
    return best

# Function to find the best move for AI
def best_move(b):
    best = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = 'X'  # Try AI move
                valm = mini(b, False)  # Evaluate using minimax
                b[i][j] = ' '  # Undo move
                if valm > best:  # Update best move
                    best, move = valm, (i, j)
    return move  # Return the best move coordinates

# ---- Main Program ----
print("Enter board rows (use X,O,space for empty):")
board = []
for i in range(3):
    row = input(f"Row {i+1}: ").strip().split()  # Input each row
    while len(row) < 3:  # Fill missing spaces
        row.append(' ')
    board.append(row[:3])  # Add to board

print_b(board)  # Display current board

m = best_move(board)  # Get best move for AI
print("Best move for AI (X): Row =", m[0], ", Col =", m[1])  # Show result


##Enter board rows (use X,O,space for empty):
#Row 1: X O X 
#Row 2: O O
#Row 3:     X
'''
The Minimax Algorithm is a decision-making algorithm used in two-player games (like Tic-Tac-Toe, Chess, or Checkers) to find the best possible move for a player assuming that the opponent also plays optimally
There are two players:
MAX → tries to maximize the score (AI player)
MIN → tries to minimize the score (opponent)
'''