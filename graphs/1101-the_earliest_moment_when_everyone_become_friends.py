#1101. The Earliest Moment When Everyone Become Friends
#Medium
#
#There are n people in a social group labeled from 0 to n - 1. You are given
#an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and
#yi will be friends at the time timestampi.
#
#Friendship is symmetric. That means if a is friends with b, then b is
#friends with a. Also, person a is acquainted with a person b if a is
#friends with b, or a is a friend of someone acquainted with b.
#
#Return the earliest time for which every person became acquainted with
#every other person. If there is no such earliest time, return -1.
#
#Example 1:
#Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],
#               [20190224,2,4],[20190301,0,3],[20190312,1,2],[20190922,4,5]],
#       n = 6
#Output: 20190301
#Explanation: All people become friends in the following order:
#20190101: 0-1, 20190104: 3-4, 20190107: 2-3-4, 20190211: 0-1-5,
#20190224: 2-3-4, 20190301: 0-1-2-3-4-5. All 6 are acquainted.
#
#Example 2:
#Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
#Output: 3
#Explanation: At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
#
#Constraints:
#    2 <= n <= 100
#    1 <= logs.length <= 10^4
#    logs[i].length == 3
#    0 <= timestampi <= 10^9
#    0 <= xi, yi <= n - 1
#    xi != yi
#    All the values timestampi are unique.
#    All the pairs (xi, yi) occur at most one time in the input.

from typing import List

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """
        Union-Find: Sort by timestamp, union friends.
        Return timestamp when all are connected.
        """
        parent = list(range(n))
        rank = [0] * n
        components = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal components
            px, py = find(x), find(y)
            if px == py:
                return False

            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1

            components -= 1
            return True

        logs.sort()

        for timestamp, x, y in logs:
            union(x, y)
            if components == 1:
                return timestamp

        return -1


class SolutionSimpleUF:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        """Simpler Union-Find without rank"""
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        logs.sort()

        for timestamp, x, y in logs:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
                n -= 1
                if n == 1:
                    return timestamp

        return -1
