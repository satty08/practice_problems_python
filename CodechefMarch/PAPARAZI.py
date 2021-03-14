try:
    t = int(input())
    while t:
        n = int(input())
        arr = list(map(int, input().split()))
        if len(arr) <= 2:
            print(1)
            continue
        ans = 1
        p, st = [], []
        for i in range(len(arr)):
            p.append([i+1, arr[i]])
        
        st.append(p[0])
        st.append(p[1])
        stlen = len(st)
        for i in range(2, n):
            while n >= 2:
                s1 = (st[stlen-1][1] - st[stlen-2][1])/(st[stlen-1][0] - st[stlen-2][0])
                s2 = (p[i][1]-st[stlen-1][1])/(p[i][0] - st[stlen-1][0])
                if s1 <= s2:
                    st.pop()
                    stlen -= 1

                else:
                    break
            st.append(p[i])
            stlen += 1
            ans = max(ans, st[stlen-1][0] - st[stlen-2][0])
                
        print(ans)
        
        t -= 1
except:
    pass