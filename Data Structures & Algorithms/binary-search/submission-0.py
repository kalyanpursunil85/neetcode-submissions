class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            print (l, " ", r)
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            if target < nums[m]:
                r = m -1
            elif target > nums[m]:
                l = m + 1
        
        return -1

        """
        0   1   2   3   4   5        
        -1  0   2   4   6   8

        """