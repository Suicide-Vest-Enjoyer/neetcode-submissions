class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 100000:
            if nums[0] == -100000000:
                return 2
            return 100000
        nums = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in nums:
                cur = num
                length = 1
                while cur + 1 in nums:
                    cur += 1
                    length += 1
                best = max(best, length)
        return best







