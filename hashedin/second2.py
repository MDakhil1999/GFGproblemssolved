def first( arr, low, high):                     
    if high >= low:  
        mid = low + (high - low)//2   
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:     
            return mid     
        elif arr[mid] == 0:         
            return first(arr, (mid + 1), high)    
        else:       
            return first(arr, low, (mid - 1)) 
    return -1

matrix = [[0,0,0,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
rows = len(matrix)
col = len(matrix[0])
ans = []
for i in range(len(matrix)):
    first1 = first(matrix[i],0,col-1)
    if first1 == -1:
        ans.append(0)
    else:
        ans.append(col-first1)
print(ans)
maxi = max(ans)
if maxi == 0:
    print(-1)
else:
    ind = ans.index(maxi)
    print(ind)
    