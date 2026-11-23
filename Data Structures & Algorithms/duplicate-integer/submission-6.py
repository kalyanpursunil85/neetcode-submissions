class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        k = defaultdict(int)
        for num in nums:
            k[num] += 1
            if k[num] > 1:
                return True
        return False
        
            