class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def fn(i, state):
            if i >= len(nums):
                result.append(state.copy())
                return
            
            state.append(nums[i])
            fn(i+1, state)
            state.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            fn(i+1, state)
        
        fn(0, [])
        return result
        