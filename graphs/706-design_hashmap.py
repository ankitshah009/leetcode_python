#706. Design HashMap
#Easy
#
#Design a HashMap without using any built-in hash table libraries.
#
#Implement the MyHashMap class:
#- MyHashMap() initializes the object with an empty map.
#- void put(int key, int value) inserts a (key, value) pair into the HashMap.
#  If the key already exists in the map, update the corresponding value.
#- int get(int key) returns the value to which the specified key is mapped,
#  or -1 if this map contains no mapping for the key.
#- void remove(key) removes the key and its corresponding value if the map
#  contains the mapping for the key.
#
#Example 1:
#Input: ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
#       [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
#Output: [null, null, null, 1, -1, null, 1, null, -1]
#
#Constraints:
#    0 <= key, value <= 10^6
#    At most 10^4 calls will be made to put, get, and remove.

class MyHashMap:
    """
    Hash map with chaining using linked list buckets.
    """

    class ListNode:
        def __init__(self, key=-1, val=-1, next=None):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self):
        self.size = 1000
        # Dummy heads for each bucket
        self.buckets = [self.ListNode() for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        curr = self.buckets[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next

        curr.next = self.ListNode(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        curr = self.buckets[idx].next

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        curr = self.buckets[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


class MyHashMapSimple:
    """Simple list-based buckets"""

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx] = [(k, v) for k, v in self.buckets[idx] if k != key]


class MyHashMapArray:
    """Direct addressing for small key range"""

    def __init__(self):
        self.data = [-1] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1
