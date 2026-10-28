class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ##this can be solved using sliding window
        ## how to do this
        n = len(s)
        l = 0
        hash_set = {}
        ans = 0
        ##using the right pointer to count the frequencies of elements into string
        for r in range(len(s)):
            hash_set[s[r]] = hash_set.get(s[r],0)+1
            while hash_set[s[r]] > 1:
                hash_set[s[l]] -= 1
            
                if hash_set[s[l]] == 0:
                    del hash_set[s[l]]
                l+= 1
            ans = max(ans, r-l+1)
        return ans



        