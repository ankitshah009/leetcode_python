#1399. Count Largest Group
#Easy
#
#You are given an integer n.
#
#Each number from 1 to n is grouped according to the sum of its digits.
#
#Return the number of groups that have the largest size.
#
#Example 1:
#Input: n = 13
#Output: 4
#Explanation: There are 9 groups in total, they are grouped according sum of
#its digits of numbers from 1 to 13:
#[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
#There are 4 groups with largest size.
#
#Example 2:
#Input: n = 2
#Output: 2
#Explanation: There are 2 groups [1], [2] of size 1.
#
#Constraints:
#    1 <= n <= 10^4

from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        Group numbers by digit sum, then count groups with max size.
        """
        def digit_sum(x: int) -> int:
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        # Count numbers in each group (by digit sum)
        group_sizes = Counter(digit_sum(i) for i in range(1, n + 1))

        # Find max size
        max_size = max(group_sizes.values())

        # Count groups with max size
        return sum(1 for size in group_sizes.values() if size == max_size)


class SolutionExplicit:
    def countLargestGroup(self, n: int) -> int:
        """More explicit version"""
        def digit_sum(x: int) -> int:
            return sum(int(d) for d in str(x))

        # Group numbers
        groups = {}
        for i in range(1, n + 1):
            ds = digit_sum(i)
            if ds not in groups:
                groups[ds] = []
            groups[ds].append(i)

        # Find largest group size
        max_size = max(len(g) for g in groups.values())

        # Count groups with largest size
        return sum(1 for g in groups.values() if len(g) == max_size)


class SolutionOptimized:
    def countLargestGroup(self, n: int) -> int:
        """
        Optimized: max digit sum for n <= 10^4 is 9+9+9+9 = 36
        Use array instead of dict.
        """
        # Max digit sum for 10000 is 1+0+0+0+0 = 1, but 9999 = 36
        counts = [0] * 37

        for i in range(1, n + 1):
            ds = 0
            x = i
            while x:
                ds += x % 10
                x //= 10
            counts[ds] += 1

        max_count = max(counts)
        return sum(1 for c in counts if c == max_count)
