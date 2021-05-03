class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        i = 1
        j = 0
        minimum_platform = 1
        needed_platform = 1
        while(i < n and j < n):
            if arr[i] > dep[j]:
                j += 1
                minimum_platform -= 1
            else:
                i += 1
                minimum_platform += 1
                needed_platform = max(needed_platform, minimum_platform)
        return needed_platform