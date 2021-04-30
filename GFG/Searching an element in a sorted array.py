class Solution:
    ##Complete this function
    def ternarySearch(self,arr,N,K):
        #Your code here
        def ternary(arr, begin, end, K):
            if end >= begin:
                mid1 = begin + (end-begin)//3
                mid2 = end - (end-begin)//3
                if (arr[mid1] == K):
                    return 1
                elif (arr[mid2] == K):
                    return 1
                elif K < arr[mid1]:
                    return ternary(arr,begin,mid1-1,K)
                elif K > arr[mid2]:
                    return ternary(arr,mid2+1,end,K)
                else:
                    return ternary(arr,mid1+1,mid2-1,K)
            return -1
        return ternary(arr,0,N-1,K)