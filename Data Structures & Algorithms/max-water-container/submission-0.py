class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        result = float("-inf")
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            result = max(result, area)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                right -= 1
        
        return result
        """
        i   0   1   2   3   4   5   6   7
        v   1   7   2   5   4   7   3   6
                *   *    

        area = 36
        """