class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)
        z = x + y
        ans = bin(z)[2:]
        return(ans)
        