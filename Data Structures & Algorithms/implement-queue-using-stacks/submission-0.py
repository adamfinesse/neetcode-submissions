class MyQueue:

    def __init__(self):
        self.front = []

    def push(self, x: int) -> None:
        self.front.append(x)

    def pop(self) -> int:
        return self.front.pop(0)

    def peek(self) -> int:
        return self.front[0]

    def empty(self) -> bool:
        return not self.front


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()