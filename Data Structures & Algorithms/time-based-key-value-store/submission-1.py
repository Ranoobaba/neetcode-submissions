from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        values = self.storage.get(key, [])   # .get avoids creating empty entries
        res = ""
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]   # valid candidate; try for a later one
                l = mid + 1
            else:
                r = mid - 1
        return res