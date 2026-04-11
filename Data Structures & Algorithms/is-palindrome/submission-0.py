class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.is_alphanumeric(s[left]):
                left += 1
            while left < right and not self.is_alphanumeric(s[right]):
                right -= 1

            if self.to_lower(s[left]) != self.to_lower(s[right]):
                return False

            left += 1
            right -= 1

        return True

    def is_alphanumeric(self, ch):
        return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')

    def to_lower(self, ch):
        if 'A' <= ch <= 'Z':
            return chr(ord(ch) + 32)
        return ch
