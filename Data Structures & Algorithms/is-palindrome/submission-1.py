class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        news = s.replace(" ", "")
        news = news.lower()
        cleaned = ''.join(char for char in news if char.isalnum())
        return cleaned == cleaned[::-1]
