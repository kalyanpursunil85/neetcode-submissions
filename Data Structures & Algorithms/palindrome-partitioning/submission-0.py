class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(t):
            left, right = 0, len(t)-1
            while left < right:
                if not t[left] == t[right]:
                    return False
                left += 1
                right -= 1
            return True

        def fn(start, state):
            if start >= len(s):
                result.append(state.copy())
                return
            for end in range(start, len(s)):
                substr = s[start: end+1]
                if is_palindrome(substr):
                    state.append(substr)
                    fn(end+1, state)
                    state.pop()
        
        fn(0, [])
        return result

