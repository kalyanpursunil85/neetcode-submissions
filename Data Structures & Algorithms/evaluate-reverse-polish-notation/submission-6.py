class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ("+", "-", "*", "/")
        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()
                if t == "+":                    
                    stack.append(first+second)
                elif t == "-":
                    
                    stack.append(first-second)
                elif t == "*":
                    stack.append(first*second)
                elif t == "/":
                    stack.append(int(first/second))
        
        return stack[-1]
