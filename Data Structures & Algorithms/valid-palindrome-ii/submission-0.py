class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                news = s[l+1:r+1]   # remove left char
                if news == news[::-1]:
                    return True
                
                news1 = s[l:r]      # remove right char
                if news1 == news1[::-1]:
                    return True
                
                return False   # IMPORTANT: stop after one mismatch
        
        return True