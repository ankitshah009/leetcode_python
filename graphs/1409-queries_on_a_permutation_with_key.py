#1409. Queries on a Permutation With Key
#Medium
#
#Given the array queries of positive integers between 1 and m, you have to
#process all queries[i] (from i=0 to i=queries.length-1) according to the
#following rules:
#    In the beginning, you have the permutation P=[1,2,3,...,m].
#    For the current i, find the position of queries[i] in the permutation P
#    (indexing from 0) and then move this at the beginning of the permutation P.
#    Notice that the position of queries[i] in P is the result for queries[i].
#
#Return an array containing the result for the given queries.
#
#Example 1:
#Input: queries = [3,1,2,1], m = 5
#Output: [2,1,2,1]
#Explanation: The queries are processed as follow:
#For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3
#to the beginning of P resulting in P=[3,1,2,4,5].
#For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1
#to the beginning of P resulting in P=[1,3,2,4,5].
#For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2
#to the beginning of P resulting in P=[2,1,3,4,5].
#For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1
#to the beginning of P resulting in P=[1,2,3,4,5].
#Therefore, the array containing the result is [2,1,2,1].
#
#Example 2:
#Input: queries = [4,1,2,2], m = 4
#Output: [3,1,2,0]
#
#Example 3:
#Input: queries = [7,5,5,8,3], m = 8
#Output: [6,5,0,7,5]
#
#Constraints:
#    1 <= m <= 10^3
#    1 <= queries.length <= m
#    1 <= queries[i] <= m

from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        """
        Simulate the process with a list.
        O(n * m) time where n = len(queries).
        """
        P = list(range(1, m + 1))
        result = []

        for q in queries:
            pos = P.index(q)
            result.append(pos)
            # Move to front
            P.pop(pos)
            P.insert(0, q)

        return result


class SolutionBIT:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        """
        Binary Indexed Tree for O(n log n) solution.
        Position each element in extended array.
        """
        n = len(queries)

        # Positions: queries can be moved to front, so need n + m slots
        # Initial position of element i is at index n + i - 1
        # When moved to front, placed at decreasing indices: n-1, n-2, ...

        # BIT to count elements before each position
        size = n + m + 1
        bit = [0] * size

        def update(i, delta=1):
            while i < size:
                bit[i] += delta
                i += i & (-i)

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        # pos[x] = current position of element x in the extended array
        pos = [0] * (m + 1)
        for i in range(1, m + 1):
            pos[i] = n + i  # Initial position
            update(pos[i])

        result = []
        next_front = n  # Next available position at front

        for q in queries:
            # Current position of q
            p = pos[q]
            # Number of elements before p
            rank = query(p - 1)
            result.append(rank)

            # Remove from current position
            update(p, -1)

            # Move to front
            pos[q] = next_front
            update(next_front)
            next_front -= 1

        return result


class SolutionDict:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        """Using dictionary to track positions"""
        # Track position of each element
        pos = {i: i - 1 for i in range(1, m + 1)}

        result = []

        for q in queries:
            result.append(pos[q])

            old_pos = pos[q]
            # All elements before old_pos shift right by 1
            for key in pos:
                if pos[key] < old_pos:
                    pos[key] += 1

            # q moves to position 0
            pos[q] = 0

        return result
