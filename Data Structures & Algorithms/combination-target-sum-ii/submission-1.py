class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(i, subset):
            if sum(subset) == target:
                result.append(subset.copy())
                return
            if i >= len(candidates) or sum(subset) > target:
                return
            
            subset.append(candidates[i])
            dfs(i+1, subset)
            subset.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
                
            dfs(i+1, subset)
        
        dfs(0, [])
        return result
