class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## the optimal solution is to count frequency of each string into a hash tables and checking if they have same frequencies
        hash_s = {}
        hash_t = {}
        for i in range(len(s)):
            hash_s[s[i]] = hash_s.get(s[i],0)+1
        for k in range(len(t)):
            hash_t[t[k]] = hash_t.get(t[k],0)+1
        if hash_s == hash_t:
            return True
        else:
            return False
        