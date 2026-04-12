class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1!=n2:
            return False
        ##building hashmaps for both strings
        hash1 = {}
        hash2 = {}
        for i in s:
            hash1[i] = hash1.get(i,0)+1
        for j in t:
            hash2[j] = hash2.get(j,0)+1
        #checking the freqeuncy of each character of s is equal to t and vice versa
        if hash1 == hash2:
            return True
        return False