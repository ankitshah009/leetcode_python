#1753. Maximum Score From Removing Stones
#Medium
#
#You are playing a solitaire game with three piles of stones of sizes a, b, and
#c respectively. Each turn you choose two different non-empty piles, take one
#stone from each, and add 1 point to your score. The game stops when there are
#fewer than two non-empty piles (meaning there are no more available moves).
#
#Given three integers a, b, and c, return the maximum score you can get.
#
#Example 1:
#Input: a = 2, b = 4, c = 6
#Output: 6
#
#Example 2:
#Input: a = 4, b = 4, c = 6
#Output: 7
#
#Example 3:
#Input: a = 1, b = 8, c = 8
#Output: 8
#
#Constraints:
#    1 <= a, b, c <= 10^5

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        """
        Greedy: always pick from two largest piles.
        Math formula: min(sum // 2, sum - max)
        """
        total = a + b + c
        max_pile = max(a, b, c)

        # If one pile is >= sum of others, we can only use sum of others
        # Otherwise, we can use total // 2 (pair everything)
        return min(total // 2, total - max_pile)


class SolutionSimulation:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        """
        Simulate the game with heap.
        """
        import heapq

        # Max heap (negate values)
        heap = [-a, -b, -c]
        heapq.heapify(heap)
        score = 0

        while True:
            # Get two largest
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if second == 0:
                break

            # Take one from each
            score += 1
            heapq.heappush(heap, -(first - 1))
            heapq.heappush(heap, -(second - 1))

        return score


class SolutionMath:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        """
        Mathematical analysis.
        """
        # Sort to have a <= b <= c
        a, b, c = sorted([a, b, c])

        # If a + b <= c, we can only use a + b moves
        if a + b <= c:
            return a + b

        # Otherwise, after using c with a and b, we pair remaining
        # Total moves = (a + b + c) // 2
        return (a + b + c) // 2
