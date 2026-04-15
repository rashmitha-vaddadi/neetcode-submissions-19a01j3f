class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##the optimal alogorithm is dutch national flag 
        ##where 3 pointers are used
        ##all 0s are pushed to right and all 2s are pushed to left
        ##and 1s are left
        low,mid=0,0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1
               
        