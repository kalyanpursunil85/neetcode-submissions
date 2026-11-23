class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v = set()
        l = 0
        m = 0
        for i, c in enumerate(s):
            while c in v:
                v.remove(s[l])
                l+=1
                
            v.add(c)
            m = max(m, len(v))
        
        return m
        