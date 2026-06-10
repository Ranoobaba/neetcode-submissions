class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        news = s.replace(" ", "")
        news = news.lower()
        cleaned = ''.join(char for char in news if char.isalnum())
        half_size = len(cleaned)//2
        seen_first = set()
        seen_second = set()
        first_half = cleaned[:half_size]
        second_half = cleaned[half_size:]
        for char in second_half:
            seen_second.add(char)
        value = len(seen_second)
        for char in first_half:
            seen_second.add(char)
        if len(seen_second) == value:
            return True
        else:
            return False

