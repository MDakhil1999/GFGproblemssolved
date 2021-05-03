def search(arr,left,right,K):
    if left<=right:
        mid = (left+right)//2
        if arr[mid] == K:
            return 1
        elif arr[mid] > K:
            return search(arr,left,mid-1,K)
        else:
            return search(arr,mid+1,right,K)
    return -1
                 
N = 5
K = 3
arr = [1,2,3,4,6]
left = 0
right = N - 1
print(search(arr,left,right,K))
