class Solution:
    def climbStairs(self, n: int) -> int:
        array = [0 for i in range(n+1)]
        if n > 0:
            array[1] = 1
        if n > 1:
            array[2] = 2
        if n > 2:
            for i in range(3,n+1):
                array[i] = array[i-1] + array[i-2]
        return array[-1]