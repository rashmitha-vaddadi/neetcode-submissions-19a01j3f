class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(1,len(nums)):
            if nums[l] == 0:
                l += 1
            elif nums[r] == 0 and nums[l]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l += 1
        for r in range(l+1,len(nums)):
            if nums[l] == 1:
                l += 1
            elif nums[r]==1 and nums[l]!=1:
                nums[l],nums[r]=nums[r],nums[l]
                l+= 1
                        