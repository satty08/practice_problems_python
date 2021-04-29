'''
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied 
by its satisfaction level  i.e.  time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
'''

def maxSatisfaction(satisfaction):
    def dp(arr):
        y = 0
        for i in range(len(arr)):
            y += arr[i]*(i+1)
            
        return y
    satisfaction.sort()
    res = 0
    for i in range(len(satisfaction)):
        x = dp(satisfaction[i:len(satisfaction)])
        res = max(res, x)
        
    return res



def findWords(board, words):
    n, m = len(board), len(board[0])
    res = set()
    for i in range(n):
        for j in range(m):
            for word in words:
                if word in res:
                    continue
                if board[i][j] != word[0]:
                    continue
                dfs(board, word, 0, i, j, res, set())
    
    return list(res)

def dfs(board, word, index, x, y, res, visited):
    if index == len(word):
        res.add(word)
        return 
    if not is_valid(board, x, y) or (x, y) in visited or board[x][y] != word[index]:
        return 
    
    visited.add((x, y))
    for dx, dy in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        nx, ny = x + dx, y + dy
        dfs(board, word, index + 1, nx, ny, res, visited)
    visited.remove((x, y))

def is_valid(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0])


board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
words = ['CODE', 'SOLO', 'RULES', 'COOL']
print(findWords(board, words))


