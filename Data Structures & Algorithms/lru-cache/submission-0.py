class ListNode:
    def __init__(self, key=-1, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _delete(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def _insert(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._delete(node)
            self._insert(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._delete(node)
            del self.cache[key]
        
        new_node = ListNode(key=key, val=value)
        self._insert(new_node)
        self.cache[key] = new_node
        if len(self.cache) > self.capacity:
            del_node = self.head.next
            self._delete(del_node)
            del self.cache[del_node.key]


        
