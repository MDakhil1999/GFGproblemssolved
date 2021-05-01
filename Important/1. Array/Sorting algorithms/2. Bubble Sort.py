arr = [64,25,12,22,11]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
print(arr)