class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        while(x < n):
            x = x*3
        if x == n:
            return True
        return False