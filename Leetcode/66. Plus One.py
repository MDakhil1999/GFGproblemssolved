class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arrstr = []
        for i in digits:
            arrstr.append(str(i))
        print(arrstr)
        x = "".join(arrstr)
        print(x)
        x = int(x)
        x = x + 1
        x = str(x)
        ans = list(map(int,x))
        print(ans)
        return ans