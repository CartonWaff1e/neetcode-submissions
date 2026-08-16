class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(filter(str.isalnum, s.lower()))
        if clean == clean[::-1]:
            return True
        return False
