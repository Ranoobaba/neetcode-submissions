class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_Dict = {')':'(','}':'{',']':'['}

        for c in s:
            if c in my_Dict:
                if stack and stack[-1] == my_Dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
            




            
            

        