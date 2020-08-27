class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        matrix = [[1],[1,1]]
        for i in range(2,numRows):
            hai = [1]
            for j in range(0,len(matrix[-1])-1):
                hai.append(matrix[-1][j] + matrix[-1][j+1])
            hai.append(1)
            matrix.append(hai)
        return matrix