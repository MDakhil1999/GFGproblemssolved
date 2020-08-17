class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for i in range(0,len(S)):
            if i == 0:
                stack.append(S[i])
            else:
                if S[i] == "(":
                    stack.append(S[i])
                else:
                    if len(stack) == 0:
                        stack.append(S[i])
                    else:
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            stack.append(S[i])
        return len(stack)