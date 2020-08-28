class Solution:
    def countBits(self, num: int) -> List[int]:
        arr = []
        for i in range(num+1):
            x = bin(i)
            y = x[2:].count("1")
            arr.append(y)
        return arr