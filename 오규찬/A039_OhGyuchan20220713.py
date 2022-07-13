class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = num ** 0.5
        
        return int(root) == root