class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #first I will track the elements and their occurances in a hashmap
        n = len(nums)
        hash_map = {}
        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1
        for i in hash_map:
            if hash_map[i] > n//2:
                return i