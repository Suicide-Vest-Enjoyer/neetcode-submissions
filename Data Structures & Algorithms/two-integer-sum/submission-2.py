class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        for i in range(len(nums)):
            pivot=target-nums[i]
            if pivot in map:
                return [map[pivot], i]
            map[nums[i]]=i