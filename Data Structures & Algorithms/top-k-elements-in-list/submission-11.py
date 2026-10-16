class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0) + 1
        
        
        
        while k > 0:
            top = max(my_dict.keys())
            res.append(top)
            del my_dict[top]
            k -= 1
        return res


        