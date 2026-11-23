class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def fn(i, subset, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            fn(i, subset, total+nums[i])

            subset.pop()
            fn(i+1, subset, total)

        fn(0, [], 0)
        return result
