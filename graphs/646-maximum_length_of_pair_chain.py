#646. Maximum Length of Pair Chain
#Medium
#
#You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and
#lefti < righti.
#
#A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be
#formed in this fashion.
#
#Return the length longest chain which can be formed.
#
#You do not need to use up all the given intervals. You can select pairs in any order.
#
#Example 1:
#Input: pairs = [[1,2],[2,3],[3,4]]
#Output: 2
#Explanation: The longest chain is [1,2] -> [3,4].
#
#Example 2:
#Input: pairs = [[1,2],[7,8],[4,5]]
#Output: 3
#Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
#
#Constraints:
#    n == pairs.length
#    1 <= n <= 1000
#    -1000 <= lefti < righti <= 1000

from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        Greedy: Sort by end point, greedily pick pairs.
        Same as activity selection problem.
        """
        pairs.sort(key=lambda x: x[1])

        count = 0
        curr_end = float('-inf')

        for start, end in pairs:
            if start > curr_end:
                count += 1
                curr_end = end

        return count


class SolutionDP:
    """DP approach O(n^2)"""

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)

        # dp[i] = longest chain ending at pairs[i]
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class SolutionBinarySearch:
    """Binary search optimization"""

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        import bisect

        pairs.sort()

        # ends[i] = smallest end point for chain of length i+1
        ends = []

        for start, end in pairs:
            # Find first chain we can extend
            idx = bisect.bisect_left(ends, start)
            if idx == len(ends):
                ends.append(end)
            elif end < ends[idx]:
                ends[idx] = end

        return len(ends)
