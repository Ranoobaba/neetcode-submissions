#return true if two strings are anagram's of each other
#anagram is a string that contains the exact same charachters as another string but order doesnt matter
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        letters_in_s = Counter(s)
        letters_in_t = Counter(t)
        if letters_in_s == letters_in_t:
            return True
        return False
        

        