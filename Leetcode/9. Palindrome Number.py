class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        arr = list(map(str,string))
        if arr == arr[::-1]:
            return True
        return False