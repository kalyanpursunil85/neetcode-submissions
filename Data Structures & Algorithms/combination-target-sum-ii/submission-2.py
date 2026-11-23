class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def fn(i, state):
            if sum(state) == target:
                result.append(state.copy())
                return
            if sum(state) > target:
                return

            if i >= len(candidates):
                return
            
            state.append(candidates[i])
            fn(i+1, state)
            state.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            fn(i+1, state)
        fn(0, [])
        return result

