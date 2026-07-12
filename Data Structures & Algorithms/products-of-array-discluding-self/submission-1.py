class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outcome = [1,0]
        result = []
        for i in nums:
            if i == 0:
                outcome[1] += 1
            else:
                outcome[0] *= i
        if outcome[1] > 1:
            for i in nums:
                result.append(0)
            return result
        
        for i in nums:
            if i == 0:
                result.append(outcome[0])
            elif outcome[1] < 1:
                result.append(outcome[0] // i)
            else:
                result.append(0)
        return result