class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #what important is that i do the count of the length at the end of loop not at the start when we do the R check 
        if s == " ":
            return 1
        l = 0
        r = 1
        sub = ""
        res = 0
        while (l < r) & (r < len(s)):
            if s[r] in sub:
                sub = s[l+1:r]
                l += 1
                r += 1
            else:
                sub += s[r]
                r += 1
                res = max(res,len(sub))
        return res
            

        