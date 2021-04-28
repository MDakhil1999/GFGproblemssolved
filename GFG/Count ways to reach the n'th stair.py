class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # code here
        arr = [1,1]
        if n == 1:
            return 1
        else:
            for i in range(2,n+1):
                arr.append(arr[-1] + arr[-2])
        return (arr[-1])%1000000007