class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #what do I need to keep track of here, the number of differnet of each char in the string and the length of the stirng 
        if len(s) != len(t):
            return False
        set_s = set(s)
        set_t = set(t)
        if set_t == set_s :
            return True
        return False
 
        