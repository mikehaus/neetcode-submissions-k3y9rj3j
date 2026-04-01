class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min = val
        else:
            if val >= self.min:
                self.stack.append(val)
            else:
                encoded = 2*val - self.min
                self.stack.append(encoded)
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        cur = self.stack.pop()
        if cur < self.min:
            old = 2 * self.min - cur
            self.min = old

    def top(self) -> int:
        if not self.stack:
            return
        cur = self.stack[-1]
        if cur < self.min:
            return self.min
        return cur

    def getMin(self) -> int:
        return self.min

        
