# Leetcode 392

# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        arr = []
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                arr.append(True)
            else:
                j += 1
        print(arr)
        if len(arr) == len(s):
            return True
        return False
