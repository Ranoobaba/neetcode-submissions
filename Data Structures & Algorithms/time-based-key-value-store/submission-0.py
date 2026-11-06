from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        #binary search here is useful on the timestamps correct.
        l = 0
        r = len(self.storage[key]) - 1
        while l <= r:
                #binary search is allowed because timestamps are increasing order so they are sorted
            middle = (l + r) // 2
            print(self.storage[key][middle][0])
            if self.storage[key][middle][0] > timestamp:
                r = middle - 1
                continue
            elif self.storage[key][middle][0] < timestamp:
                l = middle + 1
                continue
            else:
                return self.storage[key][middle][1]
        return self.storage[key][-1][1]
            
             



        
