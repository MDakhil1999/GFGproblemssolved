class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        noofrows = len(matrix)
        noofcols = len(matrix[0])
        for i in range(1,noofrows):
            for j in range(1,noofcols):
                if matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(matrix[i-1][j],matrix[i-1][j-1],matrix[i][j-1])
        ans = 0
        for i in matrix:
            for j in i:
                ans += j
        return ans