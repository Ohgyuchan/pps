class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        arr = ('aeiouAEIOU')

        a = s[:len(s)//2]
        b = s[len(s)//2:]
        
        acount = bcount = 0
        for ac, bc in zip(a,b):
            if ac in arr:
                acount +=1
            if bc in arr:
                bcount +=1
        
        if acount == bcount:
            return True
        return False
            