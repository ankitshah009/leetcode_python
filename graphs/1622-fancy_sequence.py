#1622. Fancy Sequence
#Hard
#
#Write an API that generates fancy sequences using the append, addAll, and
#multAll operations.
#
#Implement the Fancy class:
#- Fancy() Initializes the object with an empty sequence.
#- void append(val) Appends an integer val to the end of the sequence.
#- void addAll(inc) Increments all existing values in the sequence by an
#  integer inc.
#- void multAll(m) Multiplies all existing values in the sequence by an
#  integer m.
#- int getIndex(idx) Gets the current value at index idx (0-indexed) of the
#  sequence modulo 10^9 + 7. If the index is greater or equal than the length
#  of the sequence, return -1.
#
#Example 1:
#Input:
#["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
#[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
#Output:
#[null, null, null, null, null, 10, null, null, null, 26, 34, 20]
#
#Constraints:
#    1 <= val, inc, m <= 100
#    0 <= idx <= 10^5
#    At most 10^5 calls total will be made to append, addAll, multAll, and getIndex.

class Fancy:
    """
    Track transformations lazily using linear transformation y = ax + b.

    For each element, store the original value and the transformation state
    at the time of insertion. When getting, reverse the transformation.
    """
    MOD = 10**9 + 7

    def __init__(self):
        self.values = []  # Original values
        self.add = 0      # Current add offset
        self.mult = 1     # Current multiplier
        # For each element, store (add, mult) at insertion time
        self.transforms = []

    def append(self, val: int) -> None:
        self.values.append(val)
        self.transforms.append((self.add, self.mult))

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1

        val = self.values[idx]
        old_add, old_mult = self.transforms[idx]

        # Current transformation: y = mult * x + add
        # At insertion: y = old_mult * x + old_add
        # We need to find current value

        # val was inserted when transformation was (old_add, old_mult)
        # Current transformation is (add, mult)
        # The delta transformation from old to current is:
        # mult_ratio = mult / old_mult
        # The actual formula: result = mult / old_mult * (val) + (add - old_add * mult / old_mult)

        mult_ratio = self.mult * pow(old_mult, self.MOD - 2, self.MOD) % self.MOD
        result = (mult_ratio * val + self.add - old_add * mult_ratio) % self.MOD

        return result


class FancySimple:
    """
    Simpler approach: Store the inverse transformation at insertion.
    """
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mult = 1

    def append(self, val: int) -> None:
        # Store value adjusted to current transformation
        # We'll reverse the transformation when getting
        inv_mult = pow(self.mult, self.MOD - 2, self.MOD)
        adjusted = (val - self.add) * inv_mult % self.MOD
        self.seq.append(adjusted)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = self.add * m % self.MOD
        self.mult = self.mult * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.MOD


class FancyNaive:
    """
    Naive O(n) per operation approach - will TLE but shows the concept.
    """
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []

    def append(self, val: int) -> None:
        self.seq.append(val)

    def addAll(self, inc: int) -> None:
        self.seq = [(x + inc) % self.MOD for x in self.seq]

    def multAll(self, m: int) -> None:
        self.seq = [(x * m) % self.MOD for x in self.seq]

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return self.seq[idx]
