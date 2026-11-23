class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        
        max_len = 1
        for n in nums:
            if n-1 in nums:
                continue
            i = n
            res = 1
            while i+1 in nums:
                res += 1
                i+=1
                max_len = max(max_len, res)
        
        return max_len

        