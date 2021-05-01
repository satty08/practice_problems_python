try:
    t = int(input())
    while t:
        l = int(input())
        s = input()
        flag = 0
        for i in range(1, l):
            print(s[:i+1])
            if s[:i+1].count('0') == s[:i+1].count('1'):
                flag = 1
                break
            
        if flag == 0:
            print('No')
        else:
            print('Yes')
        
        t -= 1
except:
    pass