class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        best = 0
        cur = 0
        for i, v in enumerate(nums):
            if i == 0 or nums[i-1] == v - 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1
        
        return best