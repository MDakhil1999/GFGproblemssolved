test = int(input())
for t in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    matrix = []
    i = 0
    hai = []
    while i < 2*n:
        hai.append(arr[i])
        if i%2 == 1:
            matrix.append(hai)
            hai = []
        i += 1
    matrix.sort(key=lambda x:x[0])
    res = []
    for i in range(n):
        if i == 0:
            res.append(matrix[i][0])
            res.append(matrix[i][1])
            print(res)
        else:
            if matrix[i][0] > res[-1] and matrix[i][1] > res[-1]:
                res.append(matrix[i][0])
                res.append(matrix[i][1])
                print(res)
            elif matrix[i][0] <= res[-1] and matrix[i][1] > res[-1]:
                res.pop()
                res.append(matrix[i][1])
                print(res)
    for i in res:
        print(i,end= " ")
    print()
                
        