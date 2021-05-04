class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf') for i in range(amount+1)]
        arr[0] = 0
        for i in range(amount+1):
            for c in coins:
                if c <= i:
                    arr[i] = min(arr[i], arr[i-c] + 1)
        if arr[-1] == inf:
            return -1
        return arr[-1]