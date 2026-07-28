class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new= sorted(nums)
        for i in range(len(new)):
            j = i + 1
            for j in range(len(new)):
                if new[i] + new[j] == target:
                    answer = [i,j]
                    return answer
                j = j + 1
            i = i + 1

        
        