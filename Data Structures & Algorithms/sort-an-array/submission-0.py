class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ##using mergesort which uses the divide and conqure algo to divide the arrays
        ##in small induvidual arrays and merge them via sorting
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        lhalf = nums[:mid]
        rhalf = nums[mid:]
        left = self.sortArray(lhalf)
        right = self.sortArray(rhalf)
        return self.merge(left,right)
    def merge(self, left, right):
        i,j= 0,0
        new = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                new.append(left[i])
                i +=1
            else:
                new.append(right[j])
                j += 1
        new.extend(left[i:])
        new.extend(right[j:])
        return new
        