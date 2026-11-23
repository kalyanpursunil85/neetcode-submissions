class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, subset):
            if sum(subset) > target:
                return
            if sum(subset) == target:
                result.append(subset.copy())
                return
            if i >= len(nums):
                return
            subset.append(nums[i])
            dfs(i, subset)

            subset.pop()
            dfs(i+1, subset)
        
        dfs(0, [])
        return result
        