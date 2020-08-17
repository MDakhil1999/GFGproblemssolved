class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for v in collections.Counter(s).values():
            if v%2 == 0:
                ans += v
            else:
                ans += v-1
                if ans%2 == 0:
                    ans += 1
        return ans