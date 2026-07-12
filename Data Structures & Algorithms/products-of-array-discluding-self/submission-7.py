class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        result = []
        right_num = 1
        for j in range(len(nums)-1, 0, -1):
            right_num *= nums[j]
            result.append(right_num)
        result.reverse()
        result.append(1)

        for i, v in enumerate(nums):
            #result.append(int(left*right[i]))
            result[i] *= left
            left = left*v
        return result
