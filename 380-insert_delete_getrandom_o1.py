#380. Insert Delete GetRandom O(1)
#Medium
#
#Implement the RandomizedSet class:
#    RandomizedSet() Initializes the RandomizedSet object.
#    bool insert(int val) Inserts an item val into the set if not present.
#        Returns true if the item was not present, false otherwise.
#    bool remove(int val) Removes an item val from the set if present.
#        Returns true if the item was present, false otherwise.
#    int getRandom() Returns a random element from the current set of elements.
#        Each element must have the same probability of being returned.
#
#You must implement the functions of the class such that each function works in average O(1) time complexity.
#
#Example 1:
#Input: ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
#       [[], [1], [2], [2], [], [1], [2], []]
#Output: [null, true, false, true, 2, true, false, 2]
#
#Constraints:
#    -2^31 <= val <= 2^31 - 1
#    At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
#    There will be at least one element in the data structure when getRandom is called.

import random

class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}  # val -> index in list
        self.vals = []  # list of values

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False

        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False

        # Swap with last element and remove
        idx = self.val_to_idx[val]
        last_val = self.vals[-1]

        self.vals[idx] = last_val
        self.val_to_idx[last_val] = idx

        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
