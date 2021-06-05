arr = [0,0,0,0]
print(''.join(arr))

'''
A string s of lowercase English letters is given. We want to partition this string into as many parts as 
possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
'''

def partitionLabels(s):
    d = {c: i for i,c in enumerate(s)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(s):
        j = max(j, d[c])
        if i == j:
            ans.append(i-anchor+1)
            anchor = i+1
            
    return ans