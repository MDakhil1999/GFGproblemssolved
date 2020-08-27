class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        setakki = set(nums)
        if target not in setakki:
            return [-1,-1]
        first = nums.index(target)
        nums = nums[::-1]
        last = len(nums) - (nums.index(target)+1)
        return [first,last]