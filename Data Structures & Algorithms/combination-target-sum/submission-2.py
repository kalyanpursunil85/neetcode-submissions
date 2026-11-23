class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def fn(i, state):
            if sum(state) == target:
                result.append(state.copy())
                return
            if sum(state) > target:
                return
            if i >= len(nums):
                return
            
            state.append(nums[i])
            fn(i, state)
            state.pop()

            fn(i+1, state)
        
        fn(0, [])
        return result
