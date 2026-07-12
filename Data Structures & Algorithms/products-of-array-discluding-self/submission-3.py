class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        result = []
        for i, v in enumerate(nums):
            right = 1
            for j in range(len(nums)-1, i, -1):
                #print(nums[j])
                right *= nums[j]
            #print(left,right)
            result.append(left*right)
            left = left*v

        return result
