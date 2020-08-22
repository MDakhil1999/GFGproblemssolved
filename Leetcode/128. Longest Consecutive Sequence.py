class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        for i in nums:
            s.add(i)
        print(s)
        ans = 0
        for i in range(n):
            if nums[i]-1 not in s:
                j = nums[i]
                while j in s:
                    j += 1
                ans = max(ans,j-nums[i])
        return ans
        