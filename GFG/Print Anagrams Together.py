def Anagrams(words,n):
    hashTable = {}
    for i in range(n):
        x = sorted(words[i])
        x = "".join(x)
        if x not in hashTable:
            hashTable[x] = [words[i]]
        else:
            hashTable[x].append(words[i])
    ans = []
    for i in hashTable:
        x = []
        for j in hashTable[i]:
            x.append(j)
        ans.append(x)
    return ans