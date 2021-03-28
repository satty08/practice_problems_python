'''
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  
For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.
'''

class Solution:
    def wordSubsets(self,A, B):
        def count(word):
            ans = [0]*26
            for l in word:
                ans[ord(l) - ord('a')] += 1
                
            return ans
        
        bMax = [0]*26
        for b in  B:
            for i, c in enumerate(count(b)):
                bMax[i] = max(bMax[i],c)
                
        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bMax)):
                ans.append(a)
        return ans

'''
On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.

We may make the following moves:

'U' moves our position up one row, if the position exists on the board;
'D' moves our position down one row, if the position exists on the board;
'L' moves our position left one column, if the position exists on the board;
'R' moves our position right one column, if the position exists on the board;
'!' adds the character board[r][c] at our current position (r, c) to the answer.
(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.
'''

def alphabetBoardPath(target):
    xdir = ['U', 'D']
    ydir = ['L', 'R']
    x, y = 0, 0
    res = ''
    posdict = {chr(ord('a')+i):divmod(i, 5) for i in range(26)}
    for i in target:
        nx, ny = posdict[i]
        ymove = ydir[ny>y]*abs(ny-y)
        xmove = xdir[nx>x]*abs(nx-x)
        
        res += ((ymove+xmove) if nx > x else (xmove+ymove)) + '!'
        x, y = nx, ny
            
    return res

print(alphabetBoardPath('leet'))