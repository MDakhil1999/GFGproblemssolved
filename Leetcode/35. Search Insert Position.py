class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        setakki = set(nums)
        if target in setakki:
            return nums.index(target)
        i = 0
        while i < len(nums):
            if nums[i] > target:
                return i
            i += 1
        return i