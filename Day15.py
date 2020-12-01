'''
Given a string,
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''

def lengthOfLongestSubstring(A):
    start = 0
    res = 0
    charDict = {}
    for i, c in enumerate(A):
        if c in charDict and charDict[c] >= start:
            res = max(res, i-start)
            start = charDict[c]+1
        charDict[c] = i
    return max(res, i-start+1)