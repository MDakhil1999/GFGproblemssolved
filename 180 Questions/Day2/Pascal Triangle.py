#haiakhilmd

matrix = [[1],[1,1]]
for i in range(2,26):
    x = [1]
    for j in range(len(matrix[-1])-1):
        x.append(matrix[-1][j] + matrix[-1][j+1])
    x.append(1)
    matrix.append(x)

test = int(input())
for t in range(test):
    n = int(input())
    res = matrix[n-1]
    for i in res:
        print(i,end=" ")
    print()