class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) #num -> count
        l = [[] for _ in range(len(nums)+1)]
        result = []

        for num, count in freq.items():
            l[count].append(num)

       
        for i in range(len(l)-1, -1, -1):
            for g in l[i]:
                result.append(g)
                if len(result) == k:
                    return result

