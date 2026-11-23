class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        visited = set()
        left = 0
        for i, c in enumerate(s):
            
            while c in visited:
                visited.remove(s[left])
                left += 1

            visited.add(c)
            result = max(result, len(visited))
        
        return result