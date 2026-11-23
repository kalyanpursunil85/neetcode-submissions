class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            length = '{:4}'.format(len(s))
            result.append(length+s)
       
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        print(len(s))
        decoded = []
        i = 0
        while i < len(s):
            length = int(s[i: i+4])
            i += 4
            decoded.append(s[i: i+length])
            i+=length
        
        return decoded
