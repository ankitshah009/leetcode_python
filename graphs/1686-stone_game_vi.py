#1686. Stone Game VI
#Medium
#
#Alice and Bob take turns playing a game, with Alice starting first.
#
#There are n stones in a pile. On each player's turn, they can remove a stone
#from the pile and receive points based on the stone's value. Alice and Bob may
#value the stones differently.
#
#You are given two integer arrays, aliceValues and bobValues, both of length n.
#Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively,
#value the ith stone.
#
#The winner is the person with the most points after all the stones are chosen.
#If both players have the same amount of points, the game results in a draw.
#Both players will play optimally.
#
#Return:
#1 if Alice wins, -1 if Bob wins, 0 if the game results in a draw.
#
#Example 1:
#Input: aliceValues = [1,3], bobValues = [2,1]
#Output: 1
#Explanation: Alice takes stone 1 (3 points). Bob takes stone 0 (2 points).
#Alice wins 3 > 2.
#
#Example 2:
#Input: aliceValues = [1,2], bobValues = [3,1]
#Output: 0
#Explanation: If Alice takes stone 0, Alice=1, Bob=1 (draw).
#If Alice takes stone 1, Alice=2, Bob=3 (Bob wins).
#
#Example 3:
#Input: aliceValues = [2,4,3], bobValues = [1,6,7]
#Output: -1
#
#Constraints:
#    n == aliceValues.length == bobValues.length
#    1 <= n <= 10^5
#    1 <= aliceValues[i], bobValues[i] <= 100

from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        """
        Greedy: Pick stones with highest combined value (alice + bob).
        By taking a stone, player gains their value AND denies opponent theirs.
        """
        n = len(aliceValues)

        # Combine values with index
        combined = [(aliceValues[i] + bobValues[i], i) for i in range(n)]
        combined.sort(reverse=True)

        alice_score = 0
        bob_score = 0

        for turn, (_, idx) in enumerate(combined):
            if turn % 2 == 0:  # Alice's turn
                alice_score += aliceValues[idx]
            else:  # Bob's turn
                bob_score += bobValues[idx]

        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0


class SolutionZip:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        """
        Using zip for cleaner iteration.
        """
        stones = sorted(zip(aliceValues, bobValues),
                       key=lambda x: x[0] + x[1], reverse=True)

        alice = sum(a for a, b in stones[::2])
        bob = sum(b for a, b in stones[1::2])

        return (alice > bob) - (alice < bob)


class SolutionProof:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        """
        Proof of greedy strategy:
        If Alice picks stone i: she gains a[i], denies Bob b[i]
        Net advantage: a[i] + b[i]
        So stones with higher combined value should be picked first.
        """
        combined = [(a + b, a, b) for a, b in zip(aliceValues, bobValues)]
        combined.sort(reverse=True)

        a_total = sum(a for _, a, _ in combined[::2])
        b_total = sum(b for _, _, b in combined[1::2])

        if a_total > b_total:
            return 1
        elif a_total < b_total:
            return -1
        return 0


class SolutionCompact:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        """
        Compact one-liner solution.
        """
        s = sorted(zip(aliceValues, bobValues), key=sum, reverse=True)
        a, b = sum(x[0] for x in s[::2]), sum(x[1] for x in s[1::2])
        return (a > b) - (a < b)


class SolutionEnumerate:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        """
        Using enumerate for clarity.
        """
        n = len(aliceValues)
        order = sorted(range(n), key=lambda i: aliceValues[i] + bobValues[i],
                      reverse=True)

        alice = sum(aliceValues[order[i]] for i in range(0, n, 2))
        bob = sum(bobValues[order[i]] for i in range(1, n, 2))

        return 1 if alice > bob else (-1 if alice < bob else 0)
