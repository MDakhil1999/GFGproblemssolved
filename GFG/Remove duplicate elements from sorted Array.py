class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		j = 0
		i = 0
		for i in range(N-1):
		    if A[i] != A[i+1]:
		        A[j] = A[i]
		        j += 1
		A[j] = A[N-1]
		return j+1