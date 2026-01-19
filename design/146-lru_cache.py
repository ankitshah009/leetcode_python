#146. LRU Cache
#Medium
#
#Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
#Implement the LRUCache class:
#    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#    int get(int key) Return the value of the key if the key exists, otherwise return -1.
#    void put(int key, int value) Update the value of the key if the key exists. Otherwise,
#    add the key-value pair to the cache. If the number of keys exceeds the capacity from
#    this operation, evict the least recently used key.
#
#The functions get and put must each run in O(1) average time complexity.
#
#Example 1:
#Input
#["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#Output
#[null, null, null, 1, null, -1, null, -1, 3, 4]
#
#Constraints:
#    1 <= capacity <= 3000
#    0 <= key <= 10^4
#    0 <= value <= 10^5
#    At most 2 * 10^5 calls will be made to get and put.

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
