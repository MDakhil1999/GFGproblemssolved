class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stack = []
        stackind = []
        for i in range(0,len(s)):
            if i == 0:
                stack.append(s[i])
                stackind.append(i)
            else:
                if s[i] == "(":
                    stack.append(s[i])
                    stackind.append(i)
                else:
                    if len(stack) == 0:
                        stack.append(")")
                        stackind.append(i)
                    else:
                        if stack[-1] == "(":
                            stack.pop()
                            stackind.pop()
                        else:
                            stack.append(")")
                            stackind.append(i)
        print(stack)
        print(stackind)
        stackind.append(len(s))
        print(stackind)
        ansarr = []
        if stackind[0] == 0:
            for i in range(0,len(stackind)-1):
                ansarr.append(stackind[i+1] - stackind[i]-1)
        else:
            ansarr.append(stackind[0])
            for i in range(0,len(stackind)-1):
                ansarr.append(stackind[i+1] - stackind[i]-1)
        print(ansarr)
        return max(ansarr)