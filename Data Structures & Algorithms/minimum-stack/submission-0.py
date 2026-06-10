class MinStack:

    def __init__(self):
        self.arr = []
        self.size = len(self.arr)
        self.tipy = -1
    
    def isEmpty(self):
        return self.tipy == -1
    
    def push(self, val: int) -> None:
        self.tipy += 1
        print(self.arr,self.tipy)
        return self.arr.append(val)
        
    def pop(self) -> None:
        if self.tipy == -1:
            raise Exception("This is a new exception with a custom message")
        else:
            value = self.arr.pop()
            self.tipy -= 1
            return value

    def top(self) -> int:
        if self.tipy == -1:
            raise  Exception("This is a new exception with a custom message")
        else:
            return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)
        
