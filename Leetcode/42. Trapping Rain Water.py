class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        left = [0 for i in range(n)]
        if len(height) == 0:
            return 0
        leftmaxi = height[0]
        left[0] = leftmaxi
        for i in range(1,n):
            leftmaxi = max(leftmaxi,height[i])
            left[i] = leftmaxi
        print(left)
        heightrev = height[::-1]
        right = [0 for i in range(n)]
        rightmaxi = heightrev[0]
        right[0] = rightmaxi
        for i in range(1,n):
            rightmaxi = max(rightmaxi,heightrev[i])
            right[i]  =rightmaxi
        right = right[::-1]
        print(right)
        for i in range(n):
            ans += min(left[i],right[i]) - height[i]
        return ans