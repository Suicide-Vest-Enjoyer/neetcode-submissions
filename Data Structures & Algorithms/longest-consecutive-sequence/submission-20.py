#class Solution:
#    def longestConsecutive(self, nums: List[int]) -> int:
#        nums = set(nums)
#        nums = list(nums)
#        nums.sort()
#        best = 0
#        cur = 0
#        for i, v in enumerate(nums):
#            if i == 0 or nums[i-1] == v - 1:
#                cur += 1
#                best = max(best, cur)
#            else:
#                cur = 1
#        
#        return best

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        print(nums)
        best = 1
        lenght = 1

        if len(nums) == 0:
            return 0

        for num in nums:
            if num - 1 in nums:
                cur = num - 1
                lenght = 1
                continue
            else:
                cur = num
            while cur + 1 in nums:
                cur += 1
                lenght += 1

            best = max(lenght, best)

        return best








