class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = ""
        for c in s:
            if c.isalnum():
                ch += c.lower()
        if ch == ch[::-1]:
            return True
        else:
            return False