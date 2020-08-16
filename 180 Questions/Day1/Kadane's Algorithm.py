test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    maxsofar = -10000000000
    maxendinghere = 0
    for i in range(0,n):
        maxendinghere += arr[i]
        if maxsofar < maxendinghere:
            maxsofar = maxendinghere
        if maxendinghere < 0:
            maxendinghere = 0
    print(maxsofar)