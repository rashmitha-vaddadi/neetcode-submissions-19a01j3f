class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## here the logic is to find the min right side when left
        ##side is sorted and vice versa
        low = 0
        high = len(nums)-1
        ans = float('inf')
        while low<=high:
            mid = (low+high)//2
            if nums[low]<=nums[mid]:
                ans = min(nums[low],ans)
                low = mid + 1
            else:
                ans = min(nums[mid],ans)
                high = mid - 1
        return ans

        