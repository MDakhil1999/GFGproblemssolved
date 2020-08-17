class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0,len(s)):
            if i == 0:
                stack.append(s[i])
            else:
                if s[i] == "(" or s[i] == "[" or s[i] == "{":
                    stack.append(s[i])
                else:
                    if len(stack) == 0:
                        stack.append(s[i])
                    else:
                        if s[i] == ")":
                            if stack[-1] == "(":
                                stack.pop()
                            else:
                                stack.append(s[i])
                        elif s[i] == "]":
                            if stack[-1] == "[":
                                stack.pop()
                            else:
                                stack.append(s[i])
                        else:
                            if stack[-1] == "{":
                                stack.pop()
                            else:
                                stack.append(s[i])
        if len(stack) == 0:
            return True
        else:
            return False