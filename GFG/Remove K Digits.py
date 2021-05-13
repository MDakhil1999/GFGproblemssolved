class Solution:
    def removeKdigits(self, S, K):
        # code here
        if len(S) <= K:
            return 0
        stack = []
        count = 0
        for i in range(len(S)):
            if len(stack) == 0:
                stack.append(S[i])
            else:
                if S[i] >= stack[-1]:
                    stack.append(S[i])
                else:
                    while(count < K and len(stack) > 0 and S[i] < stack[-1]):
                        stack.pop()
                        count += 1
                    stack.append(S[i])
        if count < K:
            x = K - count
            y = len(stack) - x
            stack = stack[:y]
        stack = "".join(stack)
        inti = int(stack)
        return inti