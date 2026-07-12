class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = []
        right_num = 1
        for j in range(len(nums)-1, 0, -1):
            right_num *= nums[j]
            right.append(right_num)
        right.reverse()
        right.append(1)
        result = []

        for i, v in enumerate(nums):
            result.append(int(left*right[i]))
            left = left*v
        return result
