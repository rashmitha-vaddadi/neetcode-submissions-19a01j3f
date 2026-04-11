class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##using bucket sort
        ##to solve the problem in O(N) time
        ##step 1 build the frequency map
        freq_map = {}
        n = len(nums)
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i],0)+1
        ##now create a bucket ie array of n elements and place each element at its freqency - ie the index will be the frequency here
        bucket = [[]for _ in range(n+1)]
        for element, freq in freq_map.items():
            bucket[freq].append(element)
        ##now reading from the right end of the loop
        ans = []
        for i in range(n,0,-1):
            for element in bucket[i]:
                ans.append(element)
                if len(ans) == k:
                    return ans
                    
        



        


        