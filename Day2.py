'''
This problem was asked by Spotify.

There are N couples sitting in a row of length 2 * N. They are currently ordered randomly, 
but would like to rearrange themselves so that each couple's partners can sit side by side.

What is the minimum number of swaps necessary for this to happen?
'''

row = [2, 3, 7, 3, 6, 2, 7, 6]

def solve(row):
    count = 0
    i = 0
    while i < len(row):
        for j in range(i+1, len(row)):
            if row[i] == row[j]:
                temp = row[j]
                row[j] = row[i+1]
                row[i+1] = temp
                count += 1
                break
        i += 2
    return count, row
print(solve(row))
