class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if i.isalpha() == True or i.isnumeric() == True:
                if i.islower() != True:
                    arr.append(i.lower())
                else:
                    arr.append(i)
        print(arr)
        if arr == arr[::-1]:
            return True
        return False