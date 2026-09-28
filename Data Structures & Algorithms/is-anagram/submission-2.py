class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lis = sorted(list(s))
        s = ''.join(lis)
        lit = sorted(list(t))
        t = ''.join(lit)
        return s == t
        
            