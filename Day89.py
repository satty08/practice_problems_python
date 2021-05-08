def won(board):
    if (board[0][0] == board[0][1] == board[0][2]) or (board[1][0] == board[1][1] == board[1][2]) or (board[2][0] == board[2][1] == board[2][2]):
        return True
    elif (board[0][0] == board[1][0] == board[2][0]) or (board[0][1] == board[1][1] == board[2][1]) or (board[0][2] == board[1][2] == board[2][2]):
        return True
        
    elif (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        return True
        
    elif ('_' in board[0]) or ('_' in board[1]) or ('_' in board[2]):
        return 'Continue'
        
    
        
    else:
        return False


# try:
#     t = int(input())
#     while t:
#         board = []
#         for i in range(3):
#             row = list(map(str, input().split()))
#             board.append(row)
            
#         x = won(board)
#         print(board)
#         if x == True or x == False:
#             print(1)
#         elif x == 'Invalid':
#             print(3)
#         elif x == 'Continue':
#             print(2)
        
#         t -= 1
# except:
#     pass



# try:
#     t = int(input())
#     while t:
#         n, m = map(int, input().split())
#         res = 0
#         for i in range(1, n):
#             for j in range(1, n):
#                 x, y = divmod(m, i), divmod(m, j)
#                 if divmod(x, j) == divmod(y, i):
#                     res += 1
                    
#         print(res)
        
#         t -= 1 
# except:
#     pass


try:
    t = int(input())
    while t:
        arr = []
        for i in range(3):
            row = input()
            arr.append(row)
        
        X, O, blank = 0, 0, 0
        for i in range(3):
            for j in arr[i]:
                if j == 'X': X+=1
                if j == 'O': O+=1
                if j == '_': blank += 1
            
        ansX, ansO = 0, 0
        if arr[0][0] == 'X' and arr[0][1] == 'X' and arr[0][2] == 'X': ansX = 1
        if arr[1][0] == 'X' and arr[1][1] == 'X' and arr[1][2] == 'X': ansX = 1
        if arr[2][0] == 'X' and arr[2][1] == 'X' and arr[2][2] == 'X': ansX = 1
        if arr[0][0] == 'X' and arr[1][0] == 'X' and arr[2][0] == 'X': ansX = 1
        if arr[0][1] == 'X' and arr[1][1] == 'X' and arr[2][1] == 'X': ansX = 1
        if arr[0][2] == 'X' and arr[1][2] == 'X' and arr[2][2] == 'X': ansX = 1
        if arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X': ansX = 1
        if arr[0][2] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X': ansX = 1

        if arr[0][0] == 'O' and arr[0][1] == 'O' and arr[0][2] == 'O': ansO = 1
        if arr[1][0] == 'O' and arr[1][1] == 'O' and arr[1][2] == 'O': ansO = 1
        if arr[2][0] == 'O' and arr[2][1] == 'O' and arr[2][2] == 'O': ansO = 1
        if arr[0][0] == 'O' and arr[1][0] == 'O' and arr[2][0] == 'O': ansO = 1
        if arr[0][1] == 'O' and arr[1][1] == 'O' and arr[2][1] == 'O': ansO = 1
        if arr[0][2] == 'O' and arr[1][2] == 'O' and arr[2][2] == 'O': ansO = 1
        if arr[0][0] == 'O' and arr[1][1] == 'O' and arr[2][2] == 'O': ansO = 1
        if arr[0][2] == 'O' and arr[1][1] == 'O' and arr[2][0] == 'O': ansO = 1

        if ((ansX == 1 and ansO == 1) or (X-O < 0) or (X-O > 1)): print(3)
        elif (X == 0 and O == 0 and blank == 9): print(2)
        elif (ansX == 1 and ansO == 0 and X>O): print(1)
        elif (ansX == 0 and ansO == 1 and X==O): print(1)
        elif (ansX == 0 and ansO == 0 and blank == 0): print(1)
        elif (ansX == 0 and ansO == 0 and blank>0): print(2)
        else: print(3)
        
        t -= 1
except:
    pass