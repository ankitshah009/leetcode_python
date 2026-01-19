#380. Insert Delete GetRandom O(1)
#Medium
#
#Implement the RandomizedSet class:
#- RandomizedSet() Initializes the RandomizedSet object.
#- bool insert(int val) Inserts an item val into the set if not present.
#  Returns true if the item was not present, false otherwise.
#- bool remove(int val) Removes an item val from the set if present. Returns
#  true if the item was present, false otherwise.
#- int getRandom() Returns a random element from the current set of elements
#  (it's guaranteed that at least one element exists when this method is
#  called). Each element must have the same probability of being returned.
#
#You must implement the functions of the class such that each function works in
#average O(1) time complexity.
#
#Example 1:
#Input: ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove",
#        "insert", "getRandom"]
#       [[], [1], [2], [2], [], [1], [2], []]
#Output: [null, true, false, true, 2, true, false, 2]
#
#Constraints:
#    -2^31 <= val <= 2^31 - 1
#    At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
#    There will be at least one element in the data structure when getRandom is
#    called.

import random

class RandomizedSet:
    """
    Hash map + dynamic array.
    - Map stores val -> index in array
    - Array stores values for O(1) random access
    - For removal: swap with last element, then pop
    """

    def __init__(self):
        self.val_to_idx = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False

        self.val_to_idx[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False

        # Get index of element to remove
        idx = self.val_to_idx[val]
        last_val = self.values[-1]

        # Swap with last element
        self.values[idx] = last_val
        self.val_to_idx[last_val] = idx

        # Remove last element
        self.values.pop()
        del self.val_to_idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


class RandomizedSetWithDuplicates:
    """
    Extension: Allow duplicates (381. Insert Delete GetRandom O(1) - Duplicates allowed)
    Uses set for indices instead of single index.
    """

    def __init__(self):
        from collections import defaultdict
        self.val_to_indices = defaultdict(set)
        self.values = []

    def insert(self, val: int) -> bool:
        self.val_to_indices[val].add(len(self.values))
        self.values.append(val)
        return len(self.val_to_indices[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.val_to_indices[val]:
            return False

        # Get any index of val
        idx = self.val_to_indices[val].pop()
        last_val = self.values[-1]

        if idx != len(self.values) - 1:
            # Swap with last
            self.values[idx] = last_val
            self.val_to_indices[last_val].add(idx)
            self.val_to_indices[last_val].discard(len(self.values) - 1)

        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
