from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        matrix = []
        combo = combinations(arr,k)
        for i in combo:
            matrix.append(list(i))
        return matrix
        