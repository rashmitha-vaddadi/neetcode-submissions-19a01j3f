class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if (mid == 0 or nums[mid] != nums[mid - 1]) and \
               (mid == n - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]  # Fix 1: return nums[mid], not mid
            if nums[mid] == nums[mid - 1] and mid % 2 != 0:
                low = mid + 1
            elif nums[mid] == nums[mid - 1] and mid % 2 == 0:
                high = mid - 1
            elif nums[mid] == nums[mid + 1] and mid % 2 != 0:
                high = mid - 1
            elif nums[mid] == nums[mid + 1] and mid %2 == 0:
                low = mid + 1




