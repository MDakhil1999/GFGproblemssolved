class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        rep = []
        for i in nums:
            if i not in rep:
                rep.append(i)
        print(rep)
        ans = []
        for i in rep:
            if nums.count(i) == 1:
                ans.append(i)
        return ans
            