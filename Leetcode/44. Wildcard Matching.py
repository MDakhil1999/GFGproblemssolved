class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows = len(s)
        cols = len(p)
        matrix = [[0 for i in range(cols+1)] for j in range(rows+1)]
        #Base conditions
        matrix[0][0] = True
        for i in range(1,rows+1):
            matrix[i][0] = False
        for i in range(1):
            for j in range(1,cols+1):
                if p[j-1] == "*":
                    matrix[i][j] = matrix[i][j-1]
                else:
                    matrix[i][j] = False
        #Main condition
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                if s[i-1] == p[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                elif p[j-1] == "*":
                    matrix[i][j] = matrix[i-1][j] or matrix[i][j-1]
                elif p[j-1] == "?":
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = False
        return matrix[-1][-1]