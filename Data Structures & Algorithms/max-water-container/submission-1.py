class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        left = 0
        right = len(heights) - 1
        max_height = max(heights)

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height*width
            best = max(best, area)
            if max_height*width < best:
                return best
            
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return best