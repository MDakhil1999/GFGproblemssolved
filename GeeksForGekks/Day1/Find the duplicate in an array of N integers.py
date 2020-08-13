def duplicates(arr, n): 
    ans = []
    for i in range(n):
        arr[arr[i]%n] = arr[arr[i]%n] + n
    for i in range(n):
        if arr[i] >= 2*n:
            ans.append(i)
    if len(ans) == 0:
        ans.append(-1)
    return ans