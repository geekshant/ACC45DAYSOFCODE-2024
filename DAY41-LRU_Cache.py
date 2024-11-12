class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

def main():
    capacity = int(input("Enter the capacity of the LRU Cache: "))
    lru_cache = LRUCache(capacity)
    while True:
        command = input("Enter command (put <key> <value> or get <key>): ")
        if command.startswith("put"):
            _, key, value = command.split()
            lru_cache.put(int(key), int(value))
        elif command.startswith("get"):
            _, key = command.split()
            print(f"Value for key {key}: {lru_cache.get(int(key))}")
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
