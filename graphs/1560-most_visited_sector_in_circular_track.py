#1560. Most Visited Sector in a Circular Track
#Easy
#
#Given an integer n and an integer array rounds. We have a circular track which
#consists of n sectors labeled from 1 to n. A marathon will be held on this track,
#the marathon consists of m rounds. The ith round starts at sector rounds[i - 1]
#and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0]
#and ends at sector rounds[1].
#
#Return an array of the most visited sectors sorted in ascending order.
#
#Notice that you circulate the track in ascending order of sector numbers in the
#counter-clockwise direction.
#
#Example 1:
#Input: n = 4, rounds = [1,3,1,2]
#Output: [1,2]
#Explanation: The marathon starts at sector 1. The order of the visited sectors
#is as follows:
#1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3)
#So sectors 1 and 2 are visited twice and they are the most visited sectors.
#Sectors 3 and 4 are visited once.
#
#Example 2:
#Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
#Output: [2]
#
#Example 3:
#Input: n = 7, rounds = [1,3,5,7]
#Output: [1,2,3,4,5,6,7]
#
#Constraints:
#    2 <= n <= 100
#    1 <= m <= 100
#    rounds.length == m + 1
#    1 <= rounds[i] <= n
#    rounds[i] != rounds[i + 1] for 0 <= i < m

from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Key insight: Only start and end positions matter.

        The middle rounds cancel out (each sector visited equally in full laps).
        The most visited are sectors from start to end (possibly wrapping).
        """
        start = rounds[0]
        end = rounds[-1]

        if start <= end:
            # No wrap: sectors from start to end
            return list(range(start, end + 1))
        else:
            # Wrap around: sectors from 1 to end, and start to n
            return list(range(1, end + 1)) + list(range(start, n + 1))


class SolutionSimulation:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Simulation approach (for verification).
        """
        visit_count = [0] * (n + 1)

        # Count starting position
        visit_count[rounds[0]] += 1

        for i in range(1, len(rounds)):
            start = rounds[i - 1]
            end = rounds[i]

            # Move from start to end (not counting start again)
            current = start
            while current != end:
                current = current % n + 1
                visit_count[current] += 1

        # Find maximum visit count
        max_visits = max(visit_count)

        return [i for i in range(1, n + 1) if visit_count[i] == max_visits]


class SolutionExplained:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Explanation of the O(1) insight.

        Consider the marathon as multiple full laps plus a partial segment.

        In full laps, every sector is visited equally.
        The difference comes from the partial segment from start to end.

        So sectors visited one more time are:
        - If start <= end: [start, start+1, ..., end]
        - If start > end: [1, 2, ..., end] and [start, start+1, ..., n]

        Since we need ascending order, the second case becomes:
        [1, ..., end, start, ..., n] but sorted: [1, ..., end] ∪ [start, ..., n]
        """
        start, end = rounds[0], rounds[-1]

        if start <= end:
            return list(range(start, end + 1))
        else:
            # Union of [1, end] and [start, n], sorted
            return list(range(1, end + 1)) + list(range(start, n + 1))


class SolutionSet:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Using set operations.
        """
        start, end = rounds[0], rounds[-1]

        if start <= end:
            most_visited = set(range(start, end + 1))
        else:
            most_visited = set(range(1, end + 1)) | set(range(start, n + 1))

        return sorted(most_visited)
