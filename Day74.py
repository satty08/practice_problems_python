'''
You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.
'''

def bagOfTokensScore(tokens, P):
    tokens.sort()
    l, r = 0, len(tokens)-1
    ans, score = 0, 0
    while l <= r:
        if P >= tokens[l]:
            score += 1
            P -= tokens[l]
            l += 1
            ans = max(ans, score)
        elif P < tokens[r] and score > 0:
            score -= 1
            P += tokens[r]
            r -= 1
        else:
            return ans
        
    return ans

'''
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of 
the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or 
vertical cell separates between two battleships (i.e., there are no adjacent battleships).
'''

def countBattleships(board):
    grid = board
    M, N = len(board), len(board[0])
    
    def dfs(x, y):
        if x < 0 or x > M or y < 0 or y > N: return
        
        grid[x][y] = 'Y'
        if y+1 < N and grid[x][y+1] == 'X': dfs(x,y+1)
        if x+1 < M and grid[x+1][y] == 'X': dfs(x+1,y)
            
    res = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 'X':
                dfs(i, j)
                res += 1
                
    return res