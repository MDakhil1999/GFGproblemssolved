class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = 0
        for i in range(len(nums)):
            ans += nums[i]
            nums[i] = ans
        return nums