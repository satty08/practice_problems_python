'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in 
adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return 
if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
'''

def canPlaceFlowers(flowerbed, n):
    if len(flowerbed) == 0:
        return False
        
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] += 1
            count += 1
    if count >= n:
        return True
    else:
        False

