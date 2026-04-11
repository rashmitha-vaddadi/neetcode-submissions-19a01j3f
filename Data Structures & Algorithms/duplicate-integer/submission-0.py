class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ##with the sliding window concept
        k = set() ##this is the window size
        for i in range(len(nums)):
            if nums[i] in k:
                return True
            k.add(nums[i])
        return False
        