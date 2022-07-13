class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        half = len(s) // 2
        
        a = 0; b = 0
        
        a += s.count('a', 0, half)
        a += s.count('e', 0, half)
        a += s.count('i', 0, half)
        a += s.count('o', 0, half)
        a += s.count('u', 0, half)
        
        b += s.count('a', half)
        b += s.count('e', half)
        b += s.count('i', half)
        b += s.count('o', half)
        b += s.count('u', half)
        
        
        return a == b