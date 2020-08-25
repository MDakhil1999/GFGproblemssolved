class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        largest = 0
        while start != end:
            currarea = min(height[start],height[end])*(end-start)
            largest = max(largest,currarea)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return largest