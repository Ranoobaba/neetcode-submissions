class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        if len(s) % 2 != 0:
            return False
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif stack and ch == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack