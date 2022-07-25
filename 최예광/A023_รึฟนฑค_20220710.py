class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            nlist = list(map(int,list(str(num))))
            num = sum(nlist)
        return num