class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        inside = []
        length = []
        while j < len(s):
            if s[j] not in inside:
                inside.append(s[j])
                j += 1
            else:
                length.append(len(inside))
                inside = []
                i += 1
                j = i
        length.append(len(inside))
        print(length)
        return max(length)
            
        