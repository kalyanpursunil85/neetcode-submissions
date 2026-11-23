class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        # sort the array
        nums.sort() # time complexity o(n) and space complexity o(1)

        # three pointers i, j, k
        for i in range(len(nums)-1):
            j = i+ 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:                    
                    result.add((nums[i], nums[j], nums[k]))
                    j+= 1
                if total < 0: 
                    j += 1
                else:
                    k -= 1
        
        return [] if not result else [list(r) for r in result]

        
        