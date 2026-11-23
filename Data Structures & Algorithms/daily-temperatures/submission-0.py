class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        0   1   2           3           4           5               6
        30  38  30          36          35          40              28
                
        1   4   1           2           1           0               0

        [(40, 5), (38, 1), (30, 0)  ]
        """
        arr_len = len(temperatures)
        stack = [(temperatures[-1], arr_len-1)] # [(value, index)]
        
        result = [0] * arr_len
        
        for i in range(len(temperatures)-2, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            result[i] = stack[-1][1] - i if stack else 0
            stack.append((temperatures[i], i))

        return result

            
