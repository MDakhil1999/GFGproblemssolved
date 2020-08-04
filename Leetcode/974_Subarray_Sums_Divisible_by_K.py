class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        arr = [0 for i in range(K)]
        print(arr)
        x = 0
        y = 0
        for i in range(0,len(A)):
            x += A[i]
            y = x%K
            arr[y] += 1
        print(arr)
        ans = 0
        for i in range(1,len(arr)):
            if arr[i] > 1:
                ans += (arr[i]*(arr[i]-1))//2
        print(ans)
        if arr[0] > 0:
            ans += (arr[0]*(arr[0]-1))//2 + arr[0]
        return ans
            