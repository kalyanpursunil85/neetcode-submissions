class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        l = [0] * 26
        for i in range(len(s)):
            l[ord(s[i]) - ord("a")] += 1
            l[ord(t[i]) - ord("a")] -= 1
        
        return all(k==0 for k in l)
        