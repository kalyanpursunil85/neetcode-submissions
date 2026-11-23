class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def fn(i, state):
            if i >= len(nums):
                result.append(state.copy())
                return
            
            state.append(nums[i])
            fn(i+1, state)

            state.pop()
            fn(i+1, state)
        
        fn(0, [])
        return result