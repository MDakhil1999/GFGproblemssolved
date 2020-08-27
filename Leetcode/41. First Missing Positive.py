class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if i > 0:
                arr.append(i)
        print(arr)
        setakki = set(arr)
        if len(arr) == 0:
            return 1
        maxi = max(arr)
        for i in range(1,maxi+2):
            if i not in setakki:
                return i