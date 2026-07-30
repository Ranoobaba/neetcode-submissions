#we have a list of numbers and we have number called k, what we want to return is a list of k values in list that are the most frequent seen.
#my first intution is to use a hashmap mainly use counter and then we use max twice on the values of the hashmap.
#the interesting part of this question is how i can decreiment the k and make sure that the values in the array are unique
#my inital intituion is run max and then have some retry logic along the lines of if max[array] in result delete from the hashmap and call max again on the counter, until k == 0 so maybe a while loop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_frequency = Counter(nums)
        result = []
        while k > 0:
            largest, throw = max(number_frequency.items(), key=lambda x:x[1])
            print(largest, result)
            if largest not in result:
                result.append(largest)
                k -= 1
            number_frequency.pop(largest,None)
        return result

        