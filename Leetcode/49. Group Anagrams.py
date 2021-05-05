class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}
        for i in range(len(strs)):
            x = sorted(strs[i])
            x = "".join(x)
            if x not in hashTable:
                hashTable[x] = [strs[i]]
            else:
                hashTable[x].append(strs[i])
        ans = []
        for i in hashTable:
            x = []
            for j in hashTable[i]:
                x.append(j)
            ans.append(x)
        return ans