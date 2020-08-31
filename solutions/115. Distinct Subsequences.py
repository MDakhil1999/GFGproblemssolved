class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        matrix = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        for i in range(len(s) + 1):
            matrix[i][0] = 1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1] and matrix[i-1][j-1]:
                    matrix[i][j] = max(matrix[i-1][j-1]+matrix[i-1][j],matrix[i-1][j] + 1)
                else:
                    matrix[i][j] = matrix[i-1][j]
        return matrix[-1][-1]
