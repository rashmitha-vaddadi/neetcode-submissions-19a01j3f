class Solution:
    def isPalindrome(self, s: str) -> bool:
        lef , rig = 0 , len(s) - 1
        while lef < rig:
            while lef < rig and not self.is_alphanumeric(s[lef]):
                lef += 1
            while rig > lef and not self.is_alphanumeric(s[rig]):
                rig -= 1
            if s[lef].lower() != s[rig].lower():
                return False
            lef , rig = lef + 1 , rig - 1
        return True
    

    def is_alphanumeric(self, ch):
        return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')