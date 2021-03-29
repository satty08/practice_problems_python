'''
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
'''

def angleClock(hour, minutes):
    hrangle = 30
    minangle = 6
        
    if (hour == 0 or hour == 12) and minutes == 0:
        return 0
        
    if hour == 12:
        hour = 0
    if hour > 12:
        hour = hour - 12
        
    hourAngle = (hour + minutes/60)*hrangle
    minuteAngle = minutes*minangle
    if abs(minuteAngle - hourAngle) > 180:
        return 360 - abs(minuteAngle - hourAngle)
        
    return abs(minuteAngle - hourAngle)
        

hr, mint = map(int, input().split())
print(angleClock(hr, mint))