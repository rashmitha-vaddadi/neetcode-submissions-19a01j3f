class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ##previously I have used sliding window = which cannot be used
        ##to use sliding window , the array should have monotonic properties
        ##we should use hashmap and prefix sum
        prefixsum = 0
        count = 0
        hashmap = {0:1}
        for num in nums:
            prefixsum += num
            count += hashmap.get(prefixsum-k,0)
            hashmap[prefixsum] = hashmap.get(prefixsum,0)+1
        return count
        