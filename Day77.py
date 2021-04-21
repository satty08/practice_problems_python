arr = [
    1,
    2,
    3,
    [[[[[4]]]]],
    [5,[6,[7,[8]]]]
]

'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally
'''

def divisorGame(self, n):
    if n%2 == 0:
        return True
    return False

'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

def minCostClimbingStairs(self, cost):
    f1 = f2 = 0
    for i in reversed(cost):
        f1, f2 = i + min(f1, f2), f1
    return min(f1, f2)