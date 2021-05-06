class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [100000000000 for i in range(n)]
        dp[n-1] = 0
        for i in range(n-2,-1,-1):
            mini = 10000000000000
            if i+nums[i] >= n:
                for j in range(i+1,n):
                    mini = min(mini,dp[j])
            else:
                for j in range(i+1,i+nums[i]+1):
                    print(j,dp[j])
                    mini = min(mini,dp[j])
            dp[i] = mini + 1
        return dp[0]