#haiakhilmd
test = int(input())
for t in range(test):
    n,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr = arr[d:] + arr[:d]
    for i in arr:
        print(i,end=" ")
    print()