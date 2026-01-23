#1894. Find the Student that Will Replace the Chalk
#Medium
#
#There are n students in a class numbered from 0 to n - 1. The teacher will
#give each student a problem starting with the student number 0, then the
#student number 1, and so on until the teacher reaches the student number n - 1.
#After that, the teacher will restart the process, starting with the student
#number 0 again.
#
#You are given a 0-indexed integer array chalk and an integer k. There are
#initially k pieces of chalk. When the student number i is given a problem to
#solve, they will use chalk[i] pieces of chalk to solve that problem. However,
#if the current number of chalk pieces is strictly less than chalk[i], then the
#student number i will be asked to replace the chalk.
#
#Return the index of the student that will replace the chalk pieces.
#
#Example 1:
#Input: chalk = [5,1,5], k = 22
#Output: 0
#
#Example 2:
#Input: chalk = [3,4,1,2], k = 25
#Output: 1
#
#Constraints:
#    chalk.length == n
#    1 <= n <= 10^5
#    1 <= chalk[i] <= 10^5
#    1 <= k <= 10^9

from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        Find remainder after full rounds, then simulate.
        """
        total = sum(chalk)
        k %= total  # Remaining chalk after complete rounds

        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c

        return 0  # Should not reach here


class SolutionBinarySearch:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        Binary search on prefix sums.
        """
        import bisect

        n = len(chalk)
        total = sum(chalk)
        k %= total

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + chalk[i]

        # Find first index where prefix sum > k
        # That student can't be served
        idx = bisect.bisect_right(prefix, k)
        return idx - 1


class SolutionPrefixSum:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        Using prefix sum with modulo.
        """
        from itertools import accumulate

        total = sum(chalk)
        k %= total

        prefix = list(accumulate(chalk))

        for i, cum_sum in enumerate(prefix):
            if cum_sum > k:
                return i

        return 0
