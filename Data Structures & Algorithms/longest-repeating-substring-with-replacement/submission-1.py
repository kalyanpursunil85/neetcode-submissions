class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        hm = {}
        max_freq = 0
        for right in range(len(s)):
            hm[s[right]] = hm.get(s[right], 0) + 1
            max_freq = max(max_freq,  hm[s[right]])
            while right - left +1 - max_freq > k:
                hm[s[left]] -= 1
                left += 1
            
            result = max(result, right-left+1)
            

        return result
