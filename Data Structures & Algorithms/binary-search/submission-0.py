class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>target:
                h = mid - 1
            else:
                l = mid + 1
        return -1
        