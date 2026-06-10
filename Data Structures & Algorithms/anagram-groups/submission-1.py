from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for word in strs:
            print(word)
            thekey = sorted(word)
            my_dict[tuple(thekey)].append(word)
        return list(my_dict.values())


        

        
        