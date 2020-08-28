class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31:
            return 0
        if x < -1 * 2**31:
            return 0
        if x >= 0:
            x = str(x)
            x = x[::-1]
            if int(x) > 2**31:
                return 0
            return int(x)
        else:
            print("ethy")
            x = abs(x)
            x = str(x)
            x = x[::-1]
            if -1*int(x) < -1*2**31:
                return 0
            return -1*int(x)