class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new= sorted(nums)
        for i in range(len(new)):
            for j in range(i+1,len(new)):
                if new[i] + new[j] == target:
                    answer = [i,j]
                    return answer
            i = i + 1

        
        