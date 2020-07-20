class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumsofar = -10000000000000000
        maxnow = 0
        for i in range(0,len(nums)):
            maxnow += nums[i]
            sumsofar = max(maxnow,sumsofar)
            if maxnow < 0:
                maxnow = 0
        return sumsofar
        