#705. Design HashSet
#Easy
#
#Design a HashSet without using any built-in hash table libraries.
#
#Implement MyHashSet class:
#- void add(key) Inserts the value key into the HashSet.
#- bool contains(key) Returns whether the value key exists in the HashSet or not.
#- void remove(key) Removes the value key in the HashSet. If key does not exist
#  in the HashSet, do nothing.
#
#Example 1:
#Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
#        "remove", "contains"]
#       [[], [1], [2], [1], [3], [2], [2], [2], [2]]
#Output: [null, null, null, true, false, null, true, null, false]
#
#Constraints:
#    0 <= key <= 10^6
#    At most 10^4 calls will be made to add, remove, and contains.

class MyHashSet:
    """
    Simple bucket-based hash set with chaining for collision handling.
    """

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.buckets[idx]


class MyHashSetBST:
    """Using BST for each bucket for O(log n) operations"""

    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def _insert(self, node, key):
        if not node:
            return self.TreeNode(key)
        if key < node.val:
            node.left = self._insert(node.left, key)
        elif key > node.val:
            node.right = self._insert(node.right, key)
        return node

    def _search(self, node, key):
        if not node:
            return False
        if key == node.val:
            return True
        elif key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _delete(self, node, key):
        if not node:
            return None
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Find min in right subtree
            temp = node.right
            while temp.left:
                temp = temp.left
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx] = self._insert(self.buckets[idx], key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx] = self._delete(self.buckets[idx], key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self._search(self.buckets[idx], key)


class MyHashSetBitVector:
    """Bit vector for O(1) operations when key range is small"""

    def __init__(self):
        # 10^6 keys, need 10^6 bits = 125000 bytes
        self.bits = [0] * ((10**6 // 32) + 1)

    def add(self, key: int) -> None:
        idx, bit = key // 32, key % 32
        self.bits[idx] |= (1 << bit)

    def remove(self, key: int) -> None:
        idx, bit = key // 32, key % 32
        self.bits[idx] &= ~(1 << bit)

    def contains(self, key: int) -> bool:
        idx, bit = key // 32, key % 32
        return bool(self.bits[idx] & (1 << bit))
