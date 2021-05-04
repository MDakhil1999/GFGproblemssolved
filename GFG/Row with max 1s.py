class Solution:
    	def rowWithMax1s(self,arr, n, m):
		# code here
		ans = []
		for i in range(0,n):
		    zero = 0
		    for j in range(m):
		        if arr[i][j] == 0 and j == m-1:
		            ans.append(0)
		        elif arr[i][j] == 0:
		            zero += 1
		        else:
		            ans.append(m-zero)
		            break
		maxi = max(ans)
		if maxi == 0:
		    return -1
		return ans.index(maxi)