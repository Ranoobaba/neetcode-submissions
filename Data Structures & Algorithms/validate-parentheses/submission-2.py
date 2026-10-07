class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}','[':']'}
        stack = []
        if len(s) == 0:
            return True
        for bracket in s:
            while bracket in brackets.keys():
                stack.append(bracket)
            if bracket == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        
            

        