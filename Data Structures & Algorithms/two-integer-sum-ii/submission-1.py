class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        ans = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                ans += [left+1, right+1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return ans
            
        