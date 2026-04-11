class Solution:
    def findMin(self, nums: List[int]) -> int:
        ##THIS PROBLEM CAN BE SOLVED IN O(N) USING BINARY SEARCH
        n = len(nums)
        ans = float("inf") ##this answer will be storing the minimum value
        low = 0 ## zeroth index
        high = n-1
        while (low<=high):
            mid = (low+high)//2
            ##there are two parts of sorted arrays here
            ##we need to identify which part is sorted
            if nums[low] <= nums[mid]:
                ans = min(nums[low],ans)
                low = mid + 1
            else:
                ans = min(nums[mid], ans)
                high = mid - 1
        return ans

        