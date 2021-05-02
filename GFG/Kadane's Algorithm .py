class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        ##Your code here
        maxsofar = -100000000
        maxendinghere = 0
        for i in range(len(a)):
            maxendinghere += a[i]
            if maxsofar < maxendinghere:
                maxsofar = maxendinghere
            maxendinghere = max(0,maxendinghere)
        return maxsofar