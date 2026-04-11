class Solution:

    def encode(self, strs: List[str]) -> str:
        ##this will take the input strings and encode it in the 
        ##following way
        ##how will we know the input string has how many characters and how they are spaced
        ##hence we will be using delimiters to break the strings
        res = ""  # ← just this
        for k in strs:
            res += str(len(k)) + "*" + k
        return res
        ## len(s) is the number of characters the decoder will try to 
        ##read and print those characters in the list
        ##& is a deliminator , if this comes first that means there is a pause
    def decode(self, s: str) -> List[str]:
        res = [] ##empty string we will return
        i = 0 ## a pointer to read through the input string
        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1 ##if the current character is not & , j will move forward
            str_len = int(s[i:j])
            res.append(s[j+1:j+1+str_len]) ## this means 
            ##the len of the string and delimator have been crossed and the actual strings starts
            ##till j+1_+str_len
            i = j + 1 + str_len
        return res
