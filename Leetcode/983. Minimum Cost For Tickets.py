class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxi = days[-1]
        arr = [0 for i in range(maxi+1)]
        print(arr)
        setakki = set(days)
        for i in range(1,maxi+1):
            if i not in setakki:
                arr[i] = arr[i-1]
            else:
                costofprev = arr[i-1]
                costatcurrminus7 = 0
                if i >= 7:
                    costatcurrminus7 = arr[i-7]
                costofcurrminus30 = 0
                if i >= 30:
                    costofcurrminus30 = arr[i-30]
                arr[i] = min(costofprev + costs[0],costatcurrminus7 + costs[1],costofcurrminus30 + costs[2])
        print(arr)
        return arr[-1]