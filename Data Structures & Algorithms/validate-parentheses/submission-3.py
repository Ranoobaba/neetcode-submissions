class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}','[':']'}
        stack = []
        if len(s) == 0:
            return True
        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
                continue
            if bracket == brackets[stack[-1]] and stack:
                stack.pop()
            else:
                return False
        return True
        
            

        