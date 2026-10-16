class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num,0) + 1
        
        
        
        while k > 0:
            #i need the key from the max of the values
            top_k , _  = max(my_dict.items(), key= lambda kv: kv[1])
            res.append(top_k)
            del my_dict[top_k]
            k -= 1
        return res


        