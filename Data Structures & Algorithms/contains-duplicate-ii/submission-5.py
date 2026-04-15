class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0
        n = len(nums)
        seen = set()
        while r<n:
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            if (r-l)>=k:
                seen.remove(nums[l])
                l += 1
            r+=1
        return False      
        