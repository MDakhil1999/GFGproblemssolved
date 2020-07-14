# Leetcode 1344

# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        print(hour)
        print(minutes)
        if hour == 12:
            hour = 0
        hrsangle = hour*30
        minsangle = minutes*6
        print(hrsangle)
        print(minsangle)
        if hrsangle >= minsangle:
            print("greaterorequal")
            angle = hrsangle - minsangle
            print("intermediate" + str(angle))
            angle += (minutes/60)*30
            print("last" + str(angle))
        else:
            print("leass")
            angle = minsangle - hrsangle
            print("inter" + str(angle))
            angle -= (minutes/60)*30 
            print("last" + str(angle))
        if angle > 180:
            angle = 360 - angle
        return abs(angle)
