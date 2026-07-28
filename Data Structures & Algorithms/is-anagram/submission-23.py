from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_set = defaultdict(list)
        t_set = defaultdict(list)
        for i in range(len(s)):
            s_set[s[i]].append(s[i])
            t_set[t[i]].append(t[i])
        if s_set == t_set:
            return True
        return False

        