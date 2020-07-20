class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        leng = len(nums)
        for i in range(0,leng):
            if nums[abs(nums[i])] >= 0:
                nums[abs(nums[i])] = -1*nums[abs(nums[i])]
            else:
                return abs(nums[i])