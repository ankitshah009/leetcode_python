#1823. Find the Winner of the Circular Game
#Medium
#
#There are n friends that are playing a game. The friends are sitting in a
#circle and are numbered from 1 to n in clockwise order. More formally, moving
#clockwise from the ith friend brings you to the (i+1)th friend for
#1 <= i < n, and moving clockwise from the nth friend brings you to the 1st
#friend.
#
#The rules of the game are as follows:
#1. Start at the 1st friend.
#2. Count the next k friends in the clockwise direction including the friend
#   you started at. The counting wraps around the circle and may count some
#   friends more than once.
#3. The last friend you counted leaves the circle and loses the game.
#4. If there is still more than one friend in the circle, go back to step 2
#   starting from the friend immediately clockwise of the friend who just lost
#   and repeat.
#5. Else, the last friend in the circle wins the game.
#
#Given the number of friends, n, and an integer k, return the winner of the
#game.
#
#Example 1:
#Input: n = 5, k = 2
#Output: 3
#
#Example 2:
#Input: n = 6, k = 5
#Output: 1
#
#Constraints:
#    1 <= k <= n <= 500

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Josephus problem - iterative solution.
        J(n, k) = (J(n-1, k) + k) % n with J(1, k) = 0
        """
        survivor = 0  # 0-indexed position

        for i in range(2, n + 1):
            survivor = (survivor + k) % i

        return survivor + 1  # Convert to 1-indexed


class SolutionRecursive:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Recursive Josephus formula.
        """
        def josephus(n: int) -> int:
            if n == 1:
                return 0
            return (josephus(n - 1) + k) % n

        return josephus(n) + 1


class SolutionSimulation:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Direct simulation with list.
        """
        circle = list(range(1, n + 1))
        idx = 0

        while len(circle) > 1:
            idx = (idx + k - 1) % len(circle)
            circle.pop(idx)

        return circle[0]


class SolutionDeque:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Using deque for efficient rotation.
        """
        from collections import deque

        dq = deque(range(1, n + 1))

        while len(dq) > 1:
            # Rotate k-1 times (count k including start)
            dq.rotate(-(k - 1))
            dq.popleft()

        return dq[0]
