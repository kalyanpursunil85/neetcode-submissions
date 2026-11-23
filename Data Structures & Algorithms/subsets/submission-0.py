class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def fn(i, subset):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            fn(i+1, subset)
            
            subset.pop()
            fn(i+1, subset)

        fn(0, [])
        return result
            