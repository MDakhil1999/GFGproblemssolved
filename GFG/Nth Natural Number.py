class Solution:
    def findNth(self,N):
        #code here
        if N < 0:
            return 0
        if N < 9:
            return N
        ans = ""
        while(N>=9):
            x = N%9
            ans += str(x)
            N = N//9
        ans += str(N)
        ans = ans[::-1]
        return int(ans)