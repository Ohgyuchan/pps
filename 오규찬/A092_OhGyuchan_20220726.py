class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds,evens = [],[]
        for n in nums:
            if n%2: odds.append(n)
            else: evens.append(n)

        odd, even = 0, 0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=evens[even]
                even += 1
            else:
                nums[i]=odds[odd]
                odd += 1

        return nums