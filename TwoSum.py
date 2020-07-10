#Leetcode 1
#Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(nums)
        leng = len(arr)
        left = 0
        right = leng-1
        while left < right and right < leng and left >= 0:
            if arr[left] + arr[right] < target:
                left += 1
            elif arr[left] + arr[right] > target:
                right -= 1
            else:
                hai = []
                hai.append(arr[left])
                hai.append(arr[right])
                break
        ans = []
        print(hai)
        ans.append(nums.index(hai[0]))
        nums = nums[::-1]
        ans.append(leng - (nums.index(hai[1])+1))
        return ans
