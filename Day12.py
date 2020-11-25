'''
Laddu Accrual System is our new goodie distribution program. In this program, we will be distributing Laddus in place of goodies for 
your winnings and various other activities (described below), that you perform on our system. Once you collect enough number of Laddus, 
you can then redeem them to get yourself anything from a wide range of CodeChef goodies.

Let us know about various activities and amount of laddus you get corresponding to them.

Contest Win (CodeChef’s Long, Cook-Off, LTIME, or any contest hosted with us) : 300 + Bonus (Bonus = 20 - contest rank). 
Note that if your rank is > 20, then you won't get any bonus.
Top Contributor on Discuss : 300
Bug Finder : 50 - 1000 (depending on the bug severity). It may also fetch you a CodeChef internship!
Contest Hosting : 50
You can do a checkout for redeeming laddus once a month. The minimum laddus redeemable at Check Out are 200 for Indians and 400 
for the rest of the world.

You are given history of various activities of a user. The user has not redeemed any of the its laddus accrued.. Now the user just 
wants to redeem as less amount of laddus he/she can, so that the laddus can last for as long as possible. Find out for how many 
maximum number of months he can redeem the laddus.

Input
The first line of input contains a single integer T denoting number of test cases
For each test case:
First line contains an integer followed by a string denoting activities, origin respectively, where activities denotes number of 
activities of the user, origin denotes whether the user is Indian or the rest of the world. origin can be "INDIAN" or "NON_INDIAN".
For each of the next activities lines, each line contains an activity.
An activity can be of four types as defined above.
Contest Win : Input will be of form of CONTEST_WON rank, where rank denotes the rank of the user.
Top Contributor : Input will be of form of TOP_CONTRIBUTOR.
Bug Finder : Input will be of form of BUG_FOUND severity, where severity denotes the severity of the bug.
Contest Hosting : Input will be of form of CONTEST_HOSTED.

Output
For each test case, find out the maximum number of months for which the user can redeem the laddus accrued.

Constraints
1 ≤ T, activities ≤ 100
1 ≤ rank ≤ 5000
50 ≤ severity ≤ 1000
'''
# t = int(input())
# while t:
#     n, origin = input().split()
#     n = int(n)
#     laddus = 0
#     for i in range(n):
#         temp = input().split()
#         for j in range(len(temp)):
#             if temp[j] == 'CONTEST_WON':
#                 bonus = 20 - int(temp[j+1])
#                 laddus += 300 + bonus
#             elif temp[j] == 'TOP_CONTRIBUTOR':
#                 laddus += 300
#             elif temp[j] == 'BUG_FOUND':
#                 laddus += int(temp[j+1])
#             elif temp[j] == 'CONTEST_HOSTED':
#                 laddus += 50
#     if origin == 'INDIAN':
#         print(laddus//200)
#     else:
#         print(laddus//400)
#     t -= 1

'''
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
'''

def urlify(s):
    s.strip()
    s = s.split()
    res = ''
    for i in range(len(s)):
        if i != len(s) -1:
            res += s[i] + '%20'
        else:
            res += s[i]
    return res

s = '      I  am   a   boy   '
print(urlify(s))            


'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.
'''

def merge(intervals):
    ans = []
    for beg, end in sorted(intervals):
        if not ans or ans[-1][1] < beg:
            ans += [[beg, end]]
        else:
            ans[-1][1] = max(ans[-1][1], end)
                
    return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))