class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #what do I need to keep track of here, the number of differnet of each char in the string and the length of the stirng 
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        print(s,t)
        return s == t
 
        