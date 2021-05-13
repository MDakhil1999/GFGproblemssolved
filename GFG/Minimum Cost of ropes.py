#User function Template for python3
from heapq import heapify, heappush, heappop
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heap = []
        heapify(heap)
        for i in range(n):
            heappush(heap,arr[i])
        ans = 0
        for i in range(n-1):
            x = heappop(heap)
            y = heappop(heap)
            z = x + y
            ans += z
            heappush(heap,z)
        return ans