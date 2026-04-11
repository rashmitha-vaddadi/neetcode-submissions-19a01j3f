class Solution:

    def encode(self, strs: List[str]) -> str:
        ##this will take the input strings and encode it in the 
        ##following way
        ##how will we know the input string has how many characters and how they are spaced
        ##hence we will be using delimiters to break the strings
        res = ""  # ← just this
        for s in strs:
            res += str(len(s)) + "&" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "&":
                j += 1
            str_len = int(s[i:j])
            res.append(s[j+1:j+1+str_len])
            i = j + 1 + str_len
        return res
