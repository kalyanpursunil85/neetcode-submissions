class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        d = Counter(nums)
        arr = [[] for _ in range(len(nums)+1)]
        
        for num, occ in d.items():
            arr[occ].append(num)
        
        for i in range(len(arr)-1, -1, -1):
            if len(result) == k:
                return result
            else:
                if arr[i]:
                    result.extend(arr[i])

        return result