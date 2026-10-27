class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ##this can be solved by two pointer technique
        ##nums[0] + nums[n-1]<target .. this means we should skip at as max possible value ie the sum of lowest and highest number is less than target
        n = len(numbers)
        r = 0
        l = n-1
        while r <= l:
            if numbers[r]+numbers[l] == target:
                return [r+1,l+1]
            elif numbers[r]+numbers[l]>target:
                l -= 1
            else:
                r += 1

        