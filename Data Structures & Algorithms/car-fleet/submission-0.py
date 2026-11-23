class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped = sorted(zipped)
        
        p, s = zipped[-1]
        t = (target - p)/s
        stack = [t]
        for i in range(len(zipped)-2, -1, -1):
            p, s = zipped[i]
            t = (target - p)/s
            if stack and t > stack[-1]:
                stack.append(t)
        return len(stack)