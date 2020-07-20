# Leetcode 78

# https://leetcode.com/problems/subsets/

from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        array = []
        for i in range(0,len(nums)+1):
            perms = combinations(nums,i)
            for i in perms:
                array.append(list(i))      
        return array
