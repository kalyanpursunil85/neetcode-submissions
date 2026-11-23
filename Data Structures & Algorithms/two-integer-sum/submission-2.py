class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()

        for i, val in enumerate(nums):
            if target - val in lookup:
                return [lookup[target - val], i]
            else:
                lookup[val] = i
        

