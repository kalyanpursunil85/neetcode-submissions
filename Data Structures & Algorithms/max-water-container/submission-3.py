class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = float("-inf")
        left, right = 0, len(heights)-1
        while left < right:
            cur = min(heights[left], heights[right]) * (right-left)
            result = max(cur, result)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return result
        