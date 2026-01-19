#406. Queue Reconstruction by Height
#Medium
#
#You are given an array of people, people, which are the attributes of some
#people in a queue (not necessarily in order). Each people[i] = [hi, ki]
#represents the ith person of height hi with exactly ki other people in front
#who have a height greater than or equal to hi.
#
#Reconstruct and return the queue that is represented by the input array
#people. The returned queue should be formatted as an array queue, where
#queue[j] = [hj, kj] is the attributes of the jth person in the queue
#(queue[0] is the person at the front of the queue).
#
#Example 1:
#Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
#Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
#
#Example 2:
#Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
#Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
#
#Constraints:
#    1 <= people.length <= 2000
#    0 <= hi <= 10^6
#    0 <= ki < people.length
#    It is guaranteed that the queue can be reconstructed.

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Greedy approach:
        1. Sort by height descending, then by k ascending
        2. Insert each person at index k

        Key insight: When processing a shorter person, all taller people are
        already placed, so inserting at index k maintains the invariant.
        """
        # Sort: tallest first, then by k
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for person in people:
            result.insert(person[1], person)

        return result


class SolutionSegmentTree:
    """Segment tree for O(n log n) insertions"""

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height ascending, then k descending
        people.sort(key=lambda x: (x[0], -x[1]))

        n = len(people)
        result = [None] * n

        # Segment tree to find kth empty position
        tree = [0] * (4 * n)

        def build(node, start, end):
            if start == end:
                tree[node] = 1
            else:
                mid = (start + end) // 2
                build(2 * node, start, mid)
                build(2 * node + 1, mid + 1, end)
                tree[node] = tree[2 * node] + tree[2 * node + 1]

        def update(node, start, end, k):
            """Find and fill kth empty position"""
            tree[node] -= 1
            if start == end:
                return start

            mid = (start + end) // 2
            if tree[2 * node] >= k:
                return update(2 * node, start, mid, k)
            else:
                return update(2 * node + 1, mid + 1, end, k - tree[2 * node])

        build(1, 0, n - 1)

        for h, k in people:
            # Find (k+1)th empty position
            pos = update(1, 0, n - 1, k + 1)
            result[pos] = [h, k]

        return result


class SolutionBIT:
    """Binary Indexed Tree approach"""

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height ascending, then k descending
        people.sort(key=lambda x: (x[0], -x[1]))

        n = len(people)
        result = [None] * n

        # BIT to track empty positions
        bit = [0] * (n + 1)

        def update(i, delta):
            while i <= n:
                bit[i] += delta
                i += i & (-i)

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        # Initialize: all positions are empty
        for i in range(1, n + 1):
            update(i, 1)

        for h, k in people:
            # Binary search for position with k empty slots before it
            lo, hi = 1, n
            while lo < hi:
                mid = (lo + hi) // 2
                if query(mid) < k + 1:
                    lo = mid + 1
                else:
                    hi = mid

            result[lo - 1] = [h, k]
            update(lo, -1)

        return result
