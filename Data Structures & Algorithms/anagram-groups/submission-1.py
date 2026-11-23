class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for str in strs:
            l = [0]*26
            for c in str:
                l[ord(c) - ord("a")] += 1
            
            hm[tuple(l)].append(str)
        
        return hm.values()
            