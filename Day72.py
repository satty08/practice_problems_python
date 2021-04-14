'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent 
the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
'''

def readBinaryWatch(num):
    res = []
    for i in range(0,12):
        a = bin(i).count("1")
        for j in range(0,60):
            b = bin(j).count("1")
            summ = a+b

            if summ == num:
                res.append(f'{i}:{j:02d}')
                    
    return res