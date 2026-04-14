class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #first I will track the elements and their occurances in a hashmap
        n = len(nums)
        count = 0
        res = nums[0]
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        return res