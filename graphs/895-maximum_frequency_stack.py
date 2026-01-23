#895. Maximum Frequency Stack
#Hard
#
#Design a stack-like data structure to push elements to the stack and pop the
#most frequent element from the stack.
#
#Implement the FreqStack class:
#- FreqStack() constructs an empty frequency stack.
#- void push(int val) pushes val onto the top of the stack.
#- int pop() removes and returns the most frequent element in the stack.
#  - If there is a tie for the most frequent element, the element closest to
#    the stack's top is removed and returned.
#
#Example 1:
#Input: ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]
#       [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
#Output: [null,null,null,null,null,null,null,5,7,5,4]
#
#Constraints:
#    0 <= val <= 10^9
#    At most 2 * 10^4 calls will be made to push and pop.
#    It is guaranteed that there will be at least one element in the stack before calling pop.

from collections import defaultdict

class FreqStack:
    """
    Maintain frequency of each element and a stack for each frequency level.
    """
    def __init__(self):
        self.freq = defaultdict(int)  # val -> frequency
        self.group = defaultdict(list)  # frequency -> stack of vals
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.group[f].append(val)
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val


class FreqStackHeap:
    """Alternative using heap"""

    def __init__(self):
        import heapq
        self.heap = []  # (-freq, -seq, val)
        self.freq = defaultdict(int)
        self.seq = 0

    def push(self, val: int) -> None:
        import heapq
        self.freq[val] += 1
        heapq.heappush(self.heap, (-self.freq[val], -self.seq, val))
        self.seq += 1

    def pop(self) -> int:
        import heapq
        _, _, val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        return val


class FreqStackSimple:
    """Simpler implementation with explicit tracking"""

    def __init__(self):
        self.count = {}
        self.stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.count.get(val, 0) + 1
        self.count[val] = freq

        if freq not in self.stacks:
            self.stacks[freq] = []
        self.stacks[freq].append(val)

        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.count[val] -= 1

        if not self.stacks[self.max_freq]:
            self.max_freq -= 1

        return val
