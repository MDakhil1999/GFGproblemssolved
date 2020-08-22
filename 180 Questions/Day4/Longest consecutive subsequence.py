#haiakhilmd
test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    s = set()
    for i in arr:
        s.add(i)
    ans = 0
    for i in range(n):
        if arr[i]-1 not in s:
            j = arr[i]
            while j in s:
                j += 1
            ans = max(ans,j-arr[i])
    print(ans)
                
            
        
    
        
            
            
    