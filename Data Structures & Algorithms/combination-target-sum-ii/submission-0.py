class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def fn(i, subset, total):
            if total == target:
                result.append(subset.copy())
                return
            if total > target or i>=len(candidates):
                return
            
            subset.append(candidates[i])
            fn(i+1, subset, total+candidates[i])
            subset.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            fn(i+1, subset, total)
        
        fn(0, [], 0)
        
        return result