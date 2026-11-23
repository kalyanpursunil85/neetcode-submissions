class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0 
        nums = set(nums)
        result = 1
        for num in nums:
            if num - 1 in nums:
                continue
            counter = 1
            while num+1 in nums:
                num += 1
                counter+=1
                result = max(result, counter)
        
        return result
        
