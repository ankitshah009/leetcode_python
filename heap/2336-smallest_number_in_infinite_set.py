#2336. Smallest Number in Infinite Set
#Medium
#
#You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
#
#Implement the SmallestInfiniteSet class:
#    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all
#        positive integers.
#    int popSmallest() Removes and returns the smallest integer contained in the infinite set.
#    void addBack(int num) Adds a positive integer num back into the infinite set, if it
#        is not already in the infinite set.
#
#Example 1:
#Input
#["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest",
# "addBack", "popSmallest", "popSmallest", "popSmallest"]
#[[], [2], [], [], [], [1], [], [], []]
#Output
#[null, null, 1, 2, 3, null, 1, 4, 5]
#
#Explanation
#SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
#smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
#smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it.
#smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
#smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
#smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
#smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back.
#smallestInfiniteSet.popSmallest(); // return 4.
#smallestInfiniteSet.popSmallest(); // return 5.
#
#Constraints:
#    1 <= num <= 1000
#    At most 1000 calls will be made in total to popSmallest and addBack.

import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1  # Smallest number not yet popped from infinite set
        self.added_back = set()  # Numbers added back that are < current
        self.heap = []  # Min heap for added back numbers

    def popSmallest(self) -> int:
        # If there are added back numbers smaller than current
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added_back.remove(smallest)
            return smallest

        # Otherwise return current and increment
        result = self.current
        self.current += 1
        return result

    def addBack(self, num: int) -> None:
        # Only add back if it's smaller than current and not already added
        if num < self.current and num not in self.added_back:
            self.added_back.add(num)
            heapq.heappush(self.heap, num)
