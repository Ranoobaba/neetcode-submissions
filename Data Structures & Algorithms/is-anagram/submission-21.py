class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_set = set()
        t_set = set()
        for i in range(len(s)):
            s_set.add(s[i])
            t_set.add(t[i])
        if s_set == t_set:
            return True
        return False

        