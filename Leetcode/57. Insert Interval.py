class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        n = len(intervals)
        i = 0
        while i < n:
            if intervals[i][0] > newInterval[0]:
                break
            i += 1
        intervals.insert(i,newInterval)
        print(intervals)
        for i in range(len(intervals)):
            if i == 0:
                stack.append(intervals[0][0])
                stack.append(intervals[0][1])
            else:
                if intervals[i][0] > stack[-1] and intervals[i][1] > stack[-1]:
                    stack.append(intervals[i][0])
                    stack.append(intervals[i][1])
                elif intervals[i][0] <= stack[-1] and intervals[i][1] > stack[-1]:
                    stack.pop()
                    stack.append(intervals[i][1])
            print(stack)
        ans= []
        hai = []
        i = 0
        while i < len(stack):
            hai.append(stack[i])
            if i%2 != 0:
                ans.append(hai)
                hai = []
            i += 1
        print(ans)
        return ans
        