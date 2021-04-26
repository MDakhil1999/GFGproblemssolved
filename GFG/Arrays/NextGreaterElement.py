class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        stack = []
        for i in range(n):
            if len(stack) == 0:
                stack.append(i)
            else:
                while(len(stack) != 0 and arr[stack[-1]] < arr[i]):
                    x = stack.pop()
                    arr[x] = arr[i]
                stack.append(i)
        for i in range(len(stack)):
            arr[stack[i]] = -1
        return arr
