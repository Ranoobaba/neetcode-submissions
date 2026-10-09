class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #we iterate through the list of temperateures
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
            while stack and temperatures[i] > stack[-1][0]:
                _, temp1 = stack.pop()
                res[temp1]= i - temp1
            stack.append(((temperatures[i], i)))
        return res  






        

        

        