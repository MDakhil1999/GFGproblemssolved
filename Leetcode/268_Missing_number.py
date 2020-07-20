class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        actual = (leng*(leng+1))//2
        given = sum(nums)
        return actual - given