class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        d = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        if year%4 == 0 and year %100 != 0 or year%400 == 0:
            d[2] = 29
        dcount = 0
        for i in range(month):
            dcount += d[i]
        return dcount + day