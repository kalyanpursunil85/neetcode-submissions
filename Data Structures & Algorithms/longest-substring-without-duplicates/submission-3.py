class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        hm = {}
        left = 0
        for right in range(len(s)):
            if s[right] in hm and hm[s[right]] >= left:
                left = hm[s[right]] + 1

            hm[s[right]] = right
            result = max(result, right-left+1)
        
        return result
