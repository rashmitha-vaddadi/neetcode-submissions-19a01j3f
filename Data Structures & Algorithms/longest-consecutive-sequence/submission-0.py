class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ##for this i would take an hashset and add all the items into it
        ##after wards i would for ith element i would check if i-1 exsists , 
        ##if i-1 doesnt exsist then it means the counting will start from there and i would start till i find the logest
        hash_set = set(nums)
        if len(nums) == 0:
            return 0
        x = 0
        count = 0 
        max_len = 0
        for num in hash_set:
            if num - 1 not in hash_set:
                x = num
                count = 1
                while x+1 in hash_set:
                    x = x+1 
                    count += 1
                max_len = max(count,max_len)
        return max_len



        