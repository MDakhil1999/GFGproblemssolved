class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 and len(word2) == 0:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        matrix = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        print(matrix)
        for i in range(len(word2)+1):
            for j in range(len(word1)+1):
                if i == 0:
                    matrix[i][j] = j
                elif j == 0:
                    matrix[i][j] = i
        print(matrix)
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1] == word1[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = 1 + min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
        print(matrix)
        return matrix[-1][-1]