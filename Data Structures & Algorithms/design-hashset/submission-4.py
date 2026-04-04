class MyHashSet:

    def __init__(self):
        self.s = [0]

    def add(self, key: int) -> None:
        if key >= len(self.s):
            self.s.extend([0] * (key+1))
        self.s[key] = 1

    def remove(self, key: int) -> None:
        if key >= len(self.s):
            return
        self.s[key] = 0

    def contains(self, key: int) -> bool:
        if key >= len(self.s):
            return False
        return bool(self.s[key])


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)