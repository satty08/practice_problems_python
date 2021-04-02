'''
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', 
and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that 
direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white 
bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of 
available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.
'''

def numRookCaptures(board):
    row, col = 0, 0
    x, y = len(board), len(board[0])
    for i in range(len(board)):
        if 'R' in board[i]:
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    row = i
                    col = j
                    break
    res = 0
    for i in range(col, y):
        if board[row][i] == 'p':
            res += 1
            break
        elif board[row][i] == 'B':
            break
    for i in range(col, -1, -1):
        if board[row][i] == 'p':
            res += 1
            break
        elif board[row][i] == 'B':
            break
                
    for i in range(row, x):
        if board[i][col] == 'p':
            res += 1
            break
        elif board[i][col] == 'B':
            break
    for i in range(row, -1, -1):
        if board[i][col] == 'p':
            res += 1
            break
        elif board[i][col] == 'B':
            break
                
    return res

b = [[".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    ["p","p",".","R",".","p","B","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","B",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."]]
print(numRookCaptures(b))

'''
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.
'''

def average(salary):
    if len(salary) <= 2:
        return -1
    n =len(salary) - 2
    total = sum(salary) - max(salary) - min(salary)
    return total/n