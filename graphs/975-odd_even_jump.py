#975. Odd Even Jump
#Hard
#
#You are given an integer array arr. From some starting index, you can make a
#series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called
#odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps are called even-numbered.
#
#You may jump forward from index i to index j (with i < j) in the following way:
#- During odd-numbered jumps, you jump to j where arr[j] is the smallest among
#  arr[k] >= arr[i] for k > i. If multiple such j exist, pick smallest j.
#- During even-numbered jumps, you jump to j where arr[j] is the largest among
#  arr[k] <= arr[i] for k > i. If multiple such j exist, pick smallest j.
#
#Return the number of starting indices from which you can reach the end.
#
#Example 1:
#Input: arr = [10,13,12,14,15]
#Output: 2
#
#Constraints:
#    1 <= arr.length <= 2 * 10^4
#    0 <= arr[i] < 10^5

from sortedcontainers import SortedList

class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        """
        DP with sorted structure for next jump lookup.
        """
        n = len(arr)

        # next_odd[i] = index to jump to on odd jump from i
        # next_even[i] = index to jump to on even jump from i
        next_odd = [None] * n
        next_even = [None] * n

        # Process from right to left using sorted structure
        # (value, index) sorted by value
        sorted_list = SortedList()

        for i in range(n - 1, -1, -1):
            val = arr[i]

            # Odd jump: smallest arr[j] >= arr[i]
            idx = sorted_list.bisect_left((val, i))
            if idx < len(sorted_list):
                next_odd[i] = sorted_list[idx][1]

            # Even jump: largest arr[j] <= arr[i]
            idx = sorted_list.bisect_right((val, n)) - 1
            if idx >= 0 and sorted_list[idx][0] <= val:
                next_even[i] = sorted_list[idx][1]

            sorted_list.add((val, i))

        # DP: can_odd[i] = can reach end starting with odd jump from i
        can_odd = [False] * n
        can_even = [False] * n
        can_odd[-1] = can_even[-1] = True

        for i in range(n - 2, -1, -1):
            if next_odd[i] is not None:
                can_odd[i] = can_even[next_odd[i]]
            if next_even[i] is not None:
                can_even[i] = can_odd[next_even[i]]

        return sum(can_odd)


class SolutionMonotonicStack:
    """Using monotonic stack with sorting"""

    def oddEvenJumps(self, arr: list[int]) -> int:
        n = len(arr)

        def make_next(sorted_indices):
            """Monotonic stack to find next greater index."""
            result = [None] * n
            stack = []

            for i in sorted_indices:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)

            return result

        # For odd jumps: sort by (value, index)
        sorted_odd = sorted(range(n), key=lambda i: (arr[i], i))
        next_odd = make_next(sorted_odd)

        # For even jumps: sort by (-value, index)
        sorted_even = sorted(range(n), key=lambda i: (-arr[i], i))
        next_even = make_next(sorted_even)

        # DP
        can_odd = [False] * n
        can_even = [False] * n
        can_odd[-1] = can_even[-1] = True

        for i in range(n - 2, -1, -1):
            if next_odd[i] is not None:
                can_odd[i] = can_even[next_odd[i]]
            if next_even[i] is not None:
                can_even[i] = can_odd[next_even[i]]

        return sum(can_odd)
