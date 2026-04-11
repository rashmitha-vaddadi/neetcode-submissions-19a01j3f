class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = {}
        n = len(nums)
        k = n//3
        res = []
        for i in range(n):
            freq_map[nums[i]] = freq_map.get(nums[i],0)+1
        for nums[i] in freq_map:
            if freq_map[nums[i]] > k:
                res.append(nums[i])
                
        return res

        