x = 'abcd'
y = 'dcba'
print(x+y == (x+y)[::-1])

'''
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, 
so that the concatenation of the two words words[i] + words[j] is a palindrome.
'''
#Time Limit Exceed
def solve(words):
    res = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] + words[j] == (words[i]+words[j])[::-1]:
                res.append([i, j])
            
            if words[j]+words[i] == (words[j]+words[i])[::-1]:
                res.append([j, i])
    return res

#Optimed Solution:
def Solution(words):
    rmap={w[::-1]:i for i,w in enumerate(words)}
    res=[]
    for i,wrd in enumerate(words):
        rev=wrd[::-1]
        if wrd in rmap:                        # same length pair
            if rmap[wrd]!=i:                   # i and j should be distinct
                res.append((i,rmap[wrd]))
        for j in range(1,len(wrd)+1):          # first or last j characters as palindrome, other part has pair
            if wrd[:-j] in rmap and wrd[-j:]==rev[:j]:
                res.append((i,rmap[wrd[:-j]]))
            if wrd[j:] in rmap and wrd[:j]==rev[-j:]:
                res.append((rmap[wrd[j:]],i))
    return res