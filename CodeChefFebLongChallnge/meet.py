test = int(input())
while test > 0:

    p = list(map(str, input().split()))                                      #p = 12:01 AM
    n = int(input())                                                  #n = 4
    time = []                                                            
    for i in range(n):                                         # [12:00 AM 11:42 PM, 12:01 AM 11:59 AM, 12:30 AM 12:00 PM, 11:59 AM 11:59 PM]
        x = list(map(str, input().split()))                    # res = 1100
        time.append(x)
    res = ''
    # p converted to 2400 HRS
    t = 0
    pres = list(map(int, p[0].split(':')))
    if p[1] == 'AM':
        if pres[0] == 12:
            t = pres[1]
        else:
            t = pres[0]*100 + pres[1]

    elif p[1] == 'PM':
        if pres[0] == 12:
            t = pres[0]*100 + pres[1]
        else:
            t = 1200 + pres[0]*100 + pres[1]
    for i in range(n):                                    # time[i] = ['12:00', 'AM', '11:42', 'PM']
        ans = []
        for j in range(0, 4, 2):
            curr = list(map(int, time[i][j].split(':')))
            if time[i][j+1] == 'AM':
                if curr[0] == 12:
                    a = curr[1]
                else:
                    a = curr[0]*100 + curr[1]

            if time[i][j+1] == 'PM':
                if curr[0] == 12:
                    a = curr[0]*100 + curr[1]
                else:
                    a = 1200 + curr[0]*100 + curr[1]

            ans.append(a)
        if t >= ans[0] and t <= ans[1]:
            res += '1'
        else:
            res += '0'

    print(res)
    test -= 1