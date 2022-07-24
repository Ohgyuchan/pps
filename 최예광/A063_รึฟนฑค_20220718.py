class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tmp = int(a,2) + int(b,2)
        return format(tmp, 'b')