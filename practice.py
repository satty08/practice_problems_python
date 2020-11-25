n, origin = input().split()
n = int(n)
laddus = 0
for i in range(n):
    temp = input().split()
    for j in range(len(temp)):
        if temp[j] == 'CONTEST_WON':
            bonus = 20 - int(temp[j+1])
            laddus += 300 + bonus
        elif temp[j] == 'TOP_CONTRIBUTOR':
            laddus += 300
        elif temp[j] == 'BUG_FOUND':
            laddus += int(temp[j+1])
        elif temp[j] == 'CONTEST_HOSTED':
            laddus += 50
if origin == 'INDIAN':
    print(laddus//200)
else:
    print(laddus//400)