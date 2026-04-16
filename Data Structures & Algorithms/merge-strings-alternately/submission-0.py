class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        i,j=0,0
        ans =""
        while i<n1 and j<n2:
            ans = ans + word1[i]
            i += 1
            ans = ans + word2[j]
            j += 1
        if n1>n2:
            ans += word1[i:n1]
        else:
            ans += word2[j:n2]
        return ans

        