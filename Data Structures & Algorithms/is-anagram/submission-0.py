class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}

        if len(s) != len(t):
            return False
        else:
            for ch1 in s:

                if ch1 in s1:
                    s1[ch1] += 1
                else:
                    s1[ch1] = 1

            for ch2 in t:
                if ch2 in t1:
                    t1[ch2] += 1
                else:
                    t1[ch2] = 1
        if s1 == t1:
            return True
        return False


        