class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        if len(nums) < 3:
            return []

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l+=1
                elif t < 0:
                    l+=1
                else:
                    r -= 1

        return [list(r) for r in result]