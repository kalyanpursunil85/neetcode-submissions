class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        """ 
            -1,0,1,2,-1,-4
            -4, -1, -1, 0, 1, 2
        """

        nums = sorted(nums)
        l, r = 0, len(nums)-1
        result = []
        for l in range(len(nums)-2):
            j = l+1
            r = len(nums)-1
            while j<r:
                total = nums[l]+nums[j]+nums[r]
                if total < 0:
                    j+=1
                elif total > 0:
                    r-=1
                else:
                    t = [nums[l], nums[j], nums[r]]
                    if t not in result:
                        result.append(t)
                    j+=1
           
        return result

