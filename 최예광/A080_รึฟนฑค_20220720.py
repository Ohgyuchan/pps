class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = mx = idx = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count += 1
            else:
                count = 0
            if count > mx:
                mx = count
                idx = i
        return nums[idx]