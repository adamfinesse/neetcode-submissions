class ListNode:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.next = None
class MyHashMap:

    def __init__(self):
        self.m = [ListNode(-1,-1) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        node = self.m[key % len(self.m)]

        while node.next:
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next
        node.next = ListNode(key,value)

    def get(self, key: int) -> int:
        node = self.m[key % len(self.m)]

        while node.next:
            if node.next.key == key: 
                return node.next.val
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        node = self.m[key % len(self.m)]

        while node.next:
            if node.next.key == key: 
                node.next = node.next.next
                return
            node = node.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)