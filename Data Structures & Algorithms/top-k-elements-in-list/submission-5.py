#we need a counter variable in order to count the maximum value in the nums array.
#we also need to use max function on the counter and we need a way to decremenet this k, so we can go down
#we need to return the value we get from max and then delete it from the array in order to maintain the uniqueness clause

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting_numbers = Counter(nums)
        result = []
        while k > 0:
            max_number, throwaway = max(counting_numbers.items(), key=lambda x :x[1])
            if max_number in result:
                counting_numbers.pop(max_number, None)
            else:
                result.append(max_number)
                k -= 1
        return result



        