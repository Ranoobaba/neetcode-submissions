class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #so naively what I was thinking would be good here is to, 
        #if i have two loops one i and one j then I check every single posisble iterations until there is a duplicate via in (N^3) is the first time compleixty and space complexity is O(1)
        max_length = 0
        for i in range(len(s)):
            new_string = ""
            new_string += s[i]
            max_length = max(max_length, len(new_string))
            for j in range(i + 1 , len(s)):
                if s[j] in new_string:
                    break;
                else:
                    new_string += s[j]
                    max_length = max(max_length, len(new_string))
        return max_length



        