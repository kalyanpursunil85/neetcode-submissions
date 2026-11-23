class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq  = Counter(nums)
        return [x for x, _ in heapq.nlargest(k, freq.items(), key=lambda y: y[1] )]
