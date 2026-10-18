class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # so naively what I was thinking would be good here is to,
        # if i have two loops one i and one j then I check every single posisble iterations until there is a duplicate via in (N^3) is the first time compleixty and space complexity is O(1)
        # sliding window problem
        new_s = ""
        max_length = 0
        l = 0
        r = 0
        while l <= r and r < len(s):
            if s == "":
                return 0
            elif not new_s and s != "":
                new_s += s[r]
                max_length = max(max_length, r - l + 1)
                r += 1
            else:
                if s[r] not in new_s:
                    new_s += s[r]
                    max_length = max(max_length, r - l + 1)
                    r += 1
                else:
                    new_s = new_s[1:]
                    max_length = max(max_length, r - l)
                    l += 1
        return max_length
