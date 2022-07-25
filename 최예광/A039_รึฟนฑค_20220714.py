class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num = num**0.5
        if int(num) == num:
            return True
        return False