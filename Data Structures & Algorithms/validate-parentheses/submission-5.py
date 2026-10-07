class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}','[':']'}
        stack = []
        if len(s) == 0:
            return True
        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif stack and bracket == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return True
        
            

        