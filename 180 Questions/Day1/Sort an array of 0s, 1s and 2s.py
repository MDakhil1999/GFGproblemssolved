#haiakhilmd

test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    count0 = 0
    count1 = 0
    count2 = 0
    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
    ansarr = []
    for i in range(count0):
        ansarr.append(0)
    for i in range(count1):
        ansarr.append(1)
    for i in range(count2):
        ansarr.append(2)
    for i in ansarr:
        print(i,end=" ")
    print()