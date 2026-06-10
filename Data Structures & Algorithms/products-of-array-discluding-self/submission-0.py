class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #let basically multiply everything expcet the inital value, then store it and append to a new list
        #maybe lets use a hashmap for x in nums, get into the dictonary, maybe enumerate 
        #hashmap with the key as the value and product as the value of the multiplcation
        final_list = []
        for i in range(len(nums)):
            prefix_res = nums[:i]
            suffix_res = nums[i+1:]
            result_pre = 1
            result_suff = 1
            for num in prefix_res:
                result_pre *= num
            for num in suffix_res:
                result_suff *= num
            final_list.append(result_pre * result_suff)
        return final_list


        
        
            


            
            


        