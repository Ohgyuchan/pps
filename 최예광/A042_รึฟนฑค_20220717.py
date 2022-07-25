class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        for c in s:
            if c == '#':
                if len(s1) == 0:
                    continue
                else:
                    s1.pop()
            else:
                s1.append(c)
        
        s2 = []
        for c in t:
            if c == '#':
                if len(s2) == 0:
                    continue
                else:
                    s2.pop()
            else:
                s2.append(c)
        
        return s1 == s2