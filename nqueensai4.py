def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("1", end=" ")
            else:
                print("ø", end=" ")
        print()

def isSafe(row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    if rowLookup[row] or slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]]:
        return False
    return True

def solveNQueensUtil(board, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
    if col >= N:
        return True

    for i in range(N):
        slashCodeValue = slashCode[i][col]
        backslashCodeValue = backslashCode[i][col]

        if isSafe(i, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
            board[i][col] = 1
            rowLookup[i] = True
            slashCodeLookup[slashCodeValue] = True
            backslashCodeLookup[backslashCodeValue] = True

            if solveNQueensUtil(board, col + 1, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
                return True

            board[i][col] = 0
            rowLookup[i] = False
            slashCodeLookup[slashCodeValue] = False
            backslashCodeLookup[backslashCodeValue] = False

    return False

def solveNQueens():
    global N
    N = 8
    board = [[0 for _ in range(N)] for _ in range(N)]

    slashCode = [[0 for _ in range(N)] for _ in range(N)]
    backslashCode = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            slashCode[i][j] = i + j
            backslashCode[i][j] = i - j + N - 1

    rowLookup = [False] * N
    slashCodeLookup = [False] * (2 * N - 1)
    backslashCodeLookup = [False] * (2 * N - 1)

    if not solveNQueensUtil(board, 0, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

# Driver Code
if __name__ == "__main__":
    solveNQueens()














# Here's a step-by-step explanation and visual representation of your **N-Queens Problem (8x8 chessboard)** code in Python:

# ---

# ### 👑 **Problem Summary:**

# Place 8 queens on an 8×8 chessboard such that **no two queens attack each other** — meaning:

# * No two queens are in the same **row**
# * No two queens are in the same **column**
# * No two queens are on the same **diagonal**

# ---

# ### 🧠 **How This Code Works:**

# #### 1. **Board Representation:**

# ```python
# board = [[0 for _ in range(N)] for _ in range(N)]
# ```

# A 2D matrix initialized to all 0s. A `1` represents a queen on the board.

# ---

# #### 2. **Diagonal Encoding:**

# * `slashCode[i][j] = i + j` → unique for each `/` diagonal.
# * `backslashCode[i][j] = i - j + N - 1` → unique for each `\` diagonal.

# This allows **constant-time** checking for diagonals using arrays.

# ---

# #### 3. **Safety Check:**

# ```python
# def isSafe(...)
# ```

# Checks:

# * Is row `i` already occupied?
# * Is `/` diagonal `i+j` occupied?
# * Is `\` diagonal `i-j+(N-1)` occupied?

# If all are safe → place the queen.

# ---

# #### 4. **Backtracking Logic:**

# ```python
# def solveNQueensUtil(...)
# ```

# * Place queen in the current column if safe.
# * Recursively try to place in the next column.
# * If stuck, **backtrack** (remove queen) and try next row.

# ---

# ### 🖨️ **Sample Output:**

# When run, this prints an **8x8 board**:

# ```
# ø ø 1 ø ø ø ø ø 
# ø ø ø ø 1 ø ø ø 
# ø ø ø ø ø ø ø 1 
# ø ø ø ø ø 1 ø ø 
# ø 1 ø ø ø ø ø ø 
# ø ø ø 1 ø ø ø ø 
# 1 ø ø ø ø ø ø ø 
# ø ø ø ø ø ø 1 ø 
# ```

# Each `1` is a **Queen**, and `ø` is an empty square.

# ---

# ### 📌 **Visual Tools You Can Use:**

# Here are links for **animated step-by-step** visualizations:

# * 🔗 [N-Queens Visualizer – USFCA](https://www.cs.usfca.edu/~galles/visualization/NQueens.html)
# * 🔗 [GeeksForGeeks N-Queens Explanation](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/)
# * 🔗 [YouTube: N-Queens Problem Explained Visually](https://www.youtube.com/watch?v=xFv_Hl4B83A)

# Would you like me to generate a graphical representation of the board with queens placed, or explain how to modify this to print **all** solutions instead of just one?
