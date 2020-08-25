class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if i == j:
                j += 1
            elif nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1
        return i+1