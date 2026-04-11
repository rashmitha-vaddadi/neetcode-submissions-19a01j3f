class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##first I will take an hash table and add all the elements of list and their count into the hashmap
        hash_map = {}
        n = len(nums)
        ans = []
        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1
        sorted_map = sorted(hash_map.items(), key=lambda x: -x[1])
        for i in range (k):
            ans.append(sorted_map[i][0])
        return ans
        


        