class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = Counter(nums)
        # print(occurences)
        # print("----")
        a = [[] for _ in range (len(nums) + 1)]
        result = []

        for e, n in occurences.items():
            a[n].append(e)
        
        # print(a)
        for i in range(len(a)-1, -1, -1):
            # print(result)
            if len(result) == k:
                return result
            else:
                result.extend(a[i])
        


        