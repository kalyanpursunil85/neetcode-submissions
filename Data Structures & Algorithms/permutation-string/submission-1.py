class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        # if len(s1) == len(s2):
        #     return Counter(s1) == Counter(s2)

        s1_c = Counter(s1)
        s1_len = len(s1)
        for i in range(len(s2)-s1_len+1):
            s2_sub = s2[i:s1_len+i]
            if s1_c == Counter(s2_sub):
                return True
        
        return False

        