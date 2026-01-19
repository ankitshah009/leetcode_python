#354. Russian Doll Envelopes
#Hard
#
#You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
#represents the width and the height of an envelope.
#
#One envelope can fit into another if and only if both the width and height of
#one envelope are greater than the other envelope's width and height.
#
#Return the maximum number of envelopes you can Russian doll (i.e., put one
#inside the other).
#
#Note: You cannot rotate an envelope.
#
#Example 1:
#Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
#Output: 3
#Explanation: The maximum number of envelopes you can Russian doll is 3
#([2,3] => [5,4] => [6,7]).
#
#Example 2:
#Input: envelopes = [[1,1],[1,1],[1,1]]
#Output: 1
#
#Constraints:
#    1 <= envelopes.length <= 10^5
#    envelopes[i].length == 2
#    1 <= wi, hi <= 10^5

from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Sort by width ascending, height descending (for same width).
        Then find LIS on heights.

        Why descending height for same width?
        If two envelopes have same width, neither can contain the other.
        Sorting heights descending ensures we don't pick multiple envelopes
        with same width in our LIS.
        """
        # Sort by width ascending, height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Find LIS on heights using binary search
        heights = [e[1] for e in envelopes]
        tails = []

        for h in heights:
            pos = bisect.bisect_left(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h

        return len(tails)


class SolutionDP:
    """O(n^2) DP approach - TLE for large inputs"""

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        envelopes.sort()
        n = len(envelopes)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if (envelopes[j][0] < envelopes[i][0] and
                    envelopes[j][1] < envelopes[i][1]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class SolutionSegmentTree:
    """Using segment tree for LIS with constraints"""

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Coordinate compression for heights
        heights = sorted(set(e[1] for e in envelopes))
        height_to_idx = {h: i for i, h in enumerate(heights)}

        # Sort envelopes
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Segment tree for range maximum query
        n = len(heights)
        tree = [0] * (2 * n)

        def update(idx, val):
            idx += n
            tree[idx] = max(tree[idx], val)
            while idx > 1:
                idx //= 2
                tree[idx] = max(tree[2 * idx], tree[2 * idx + 1])

        def query(left, right):  # [left, right)
            result = 0
            left += n
            right += n
            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                left //= 2
                right //= 2
            return result

        max_dolls = 0

        for w, h in envelopes:
            idx = height_to_idx[h]
            # Query maximum dolls for heights < h
            prev_max = query(0, idx)
            curr = prev_max + 1
            max_dolls = max(max_dolls, curr)
            update(idx, curr)

        return max_dolls
