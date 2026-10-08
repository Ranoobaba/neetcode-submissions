import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        storage = {'+':operator.add,'*':operator.mul,'-':operator.sub,'/':operator.truediv}
        for char in tokens:
            if char in "+*-/":
                second_value = stack.pop()
                first_value = stack.pop()
                operation = storage[char]
                finish = operation(int(first_value),int(second_value))
                stack.append(finish)
            else:
                stack.append(char)
        
        return int(stack[-1])

        