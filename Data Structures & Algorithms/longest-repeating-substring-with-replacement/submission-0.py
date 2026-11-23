class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        occurrences = defaultdict(int)
        for i, c in enumerate(s):
            occurrences[c] += 1
            max_value = max(occurrences.values())

            while i - left + 1 - max_value > k:
                occurrences[s[left]] -= 1
                left += 1
            
            result = max(i-left+1, result)
        
        return result
