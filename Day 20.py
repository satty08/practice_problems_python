'''
Increasing COVID cases have created panic amongst the people of Chefland, so the government is 
starting to push for production of a vaccine. It has to report to the media about the exact date 
when vaccines will be available.

There are two companies which are producing vaccines for COVID. Company A starts producing vaccines 
on day D1 and it can produce V1 vaccines per day. Company B starts producing vaccines on day D2 and 
it can produce V2 vaccines per day. Currently, we are on day 1.

We need a total of P vaccines. How many days are required to produce enough vaccines? Formally, 
find the smallest integer d such that we have enough vaccines at the end of the day d.
'''

d1, v1, d2, v2, p = map(int, input().split())
sum = 0
flag = 0
if d1<d2:
    day = d1-1
    while sum<p:
        sum += v1
        if d1==d2 or flag==1:
            sum+=v2
            flag=1
        d1 += 1
        day += 1
    print(day)
else:
    day = d2-1
    while sum<p:
        sum += v2
        if d1==d2 or flag==1:
            sum+=v1
            flag=1
        d2 += 1
        day += 1
    print(day)