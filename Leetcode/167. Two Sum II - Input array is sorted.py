class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leng = len(numbers)
        left = 0
        right = leng - 1
        ans = []
        while left < right and left >= 0 and right < leng:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                ans.append(left+1)
                ans.append(right+1)
                return ans
        