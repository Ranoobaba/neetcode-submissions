class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #we iterate through the list of temperateures
        res = []
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
                elif j == len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
                    res.append(0)
        return res



        

        