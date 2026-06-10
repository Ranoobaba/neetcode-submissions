class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #what do I need to keep track of here, the number of differnet of each char in the string and the length of the stirng 
        if len(s) != len(t):
            return False
        count = [0] * 26 
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
 
        if any(c != 0 for c in count):
            return False
        else:
            return True
        