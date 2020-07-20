def repeating(arr):
    for i in range(0,len(arr)):
        if arr[abs(arr[i])-1] >= 0:
            arr[abs(arr[i])-1] *= -1
        else:
            print(abs(arr[i]),end=" ")
    for i in range(0,len(arr)):
        if arr[i] > 0:
            print(i+1)

test = int(input())
for t in range(test):
    n = int(input())
    arr = input().split()
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    ans = []
    repeating(arr)