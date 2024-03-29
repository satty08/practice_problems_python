'''
On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.
'''

def brokenCalc(self, X: int, Y: int) -> int:
    count = 0
    while Y > X:
        count += 1
        if Y%2:
            Y += 1
        else:
            Y /= 2 
                
    return int(count + X - Y)