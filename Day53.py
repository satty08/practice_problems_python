'''
There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.

What is the maximum number of houses you can buy?
'''

t = int(input())
while t:
    n, b = map(int, input().split())
    arrN = list(map(int, input().split()))
    arrN.sort()
    ans = 0
    i = 0
    while i < len(arrN):
        b = b - arrN[i]
        if b > 0:
            ans += 1
        else:
            break
        i += 1
            
    print(ans)
    
    t -= 1

'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

'''

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        self.hash[key] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hash:
            return self.hash[key]
        return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hash:
            self.hash.pop(key)
            return
        return -1
