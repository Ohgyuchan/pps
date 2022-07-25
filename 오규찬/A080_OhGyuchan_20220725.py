class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums) / 2
        
        a = set(nums)
        
        for i in a :
            if nums.count(i) >= m :
                return i
        return 0