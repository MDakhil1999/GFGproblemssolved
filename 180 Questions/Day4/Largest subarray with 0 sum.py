def maxLen(n, arr):
    #Code here
    hashmap = {}
    maxlen = 0
    currsum = 0
    for i in range(n):
        currsum += arr[i]
        if currsum == 0:
            maxlen = i + 1
        if currsum in hashmap:
            maxlen = max(maxlen,i-hashmap[currsum])
        else:
            hashmap[currsum] = i
    return maxlen