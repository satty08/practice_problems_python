'''
Covid-19 is spreading fast! There are N cities, numbered from 0 to (N−1), arranged in a circular manner. City 0 is connected to 
city 1, 1 to 2, …, city (N−2) to city (N−1), and city (N−1) to city 0.

The virus is currently at city X. Each day, it jumps from its current city, to the city K to its right, i.e., from city X to the 
city (X+K)%N. As the virus jumps, the cities in between don't get infected. Cities once infected stay infected. You live in city Y. 
Find if it will reach your city eventually. If it will, print YES, else print NO.
'''

N, K, X, Y = 12, 3, 4, 2
l = []
l.append(X)
while True:
    X = (X+K)%N
    if X == Y:
        print('Yes')
        break
    elif X not in l:
        l.append(X)
    elif X in l:
        print('No')
        break 