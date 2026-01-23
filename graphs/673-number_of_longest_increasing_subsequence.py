#673. Number of Longest Increasing Subsequence
#Medium
#
#Given an integer array nums, return the number of longest increasing subsequences.
#
#Notice that the sequence has to be strictly increasing.
#
#Example 1:
#Input: nums = [1,3,5,4,7]
#Output: 2
#Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
#
#Example 2:
#Input: nums = [2,2,2,2,2]
#Output: 5
#Explanation: The length of the longest increasing subsequence is 1, and there are
#5 increasing subsequences of length 1.
#
#Constraints:
#    1 <= nums.length <= 2000
#    -10^6 <= nums[i] <= 10^6

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        DP: Track both length and count of LIS ending at each position.
        """
        n = len(nums)
        if n == 0:
            return 0

        # length[i] = length of LIS ending at i
        # count[i] = number of LIS of that length ending at i
        length = [1] * n
        count = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)
        return sum(c for l, c in zip(length, count) if l == max_len)


class SolutionSegmentTree:
    """Segment tree for O(n log n) solution"""

    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Coordinate compression
        sorted_unique = sorted(set(nums))
        rank = {v: i for i, v in enumerate(sorted_unique)}

        n = len(sorted_unique)

        # Segment tree: each node stores (max_length, count)
        tree = [(0, 1)] * (2 * n)

        def merge(a, b):
            if a[0] > b[0]:
                return a
            if b[0] > a[0]:
                return b
            return (a[0], a[1] + b[1])

        def update(i, val):
            i += n
            tree[i] = merge(tree[i], val)
            while i > 1:
                i //= 2
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def query(l, r):
            """Query max in range [l, r)"""
            res = (0, 1)
            l += n
            r += n
            while l < r:
                if l & 1:
                    res = merge(res, tree[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res = merge(res, tree[r])
                l //= 2
                r //= 2
            return res

        for num in nums:
            r = rank[num]
            # Query all elements with smaller rank
            length, count = query(0, r)
            # Update with (length + 1, count)
            update(r, (length + 1, max(count, 1)))

        return query(0, n)[1]


class SolutionBinarySearch:
    """Binary search with buckets"""

    def findNumberOfLIS(self, nums: List[int]) -> int:
        import bisect

        if not nums:
            return 0

        # decks[i] = list of (value, count) pairs for LIS of length i+1
        decks = []

        def get_count_sum(deck, val):
            """Sum of counts for values >= val in deck"""
            idx = bisect.bisect_left(deck, (-val, 0))
            return sum(c for v, c in deck[idx:])

        for num in nums:
            # Find deck to place this card (binary search)
            lo, hi = 0, len(decks)
            while lo < hi:
                mid = (lo + hi) // 2
                if decks[mid][-1][0] < num:
                    lo = mid + 1
                else:
                    hi = mid

            # Count combinations from previous deck
            if lo == 0:
                count = 1
            else:
                count = get_count_sum(decks[lo - 1], num)

            # Add to deck (using negative for reverse sorting)
            if lo == len(decks):
                decks.append([])
            decks[lo].append((-num, count))

        return sum(c for v, c in decks[-1])
