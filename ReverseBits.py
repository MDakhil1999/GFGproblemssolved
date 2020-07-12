# Leetcode 190

# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:        
        x = bin(n)
        x = x[2:]
        leng = len(x)
        bakki = 32-leng
        s = ""
        for i in range(0,bakki):
            s += "0"
        x = s + x
        x = x[::-1]
        return int(x,2)
