class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            l = [0]*26
            for c in s:
                l[ord(c)-ord("a")]+=1
            mapping[tuple(l)].append(s)
        
        return mapping.values()

        