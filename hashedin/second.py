matrix = [[0,0,0,1],[0,0,1,1],[1,1,1,1],[0,0,0,0]]
ans = []
for i in range(len(matrix)):
    noofzero = 0
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0 and j == len(matrix)-1:
            ans.append(0)
        elif matrix[i][j] == 0:
            noofzero += 1
        else:
            ans.append(len(matrix[0]) - j)
            break
print(ans)
maxi = max(ans)
if maxi == 0:
    print(-1)
else:
    ind = ans.index(maxi)
    print(ind)
