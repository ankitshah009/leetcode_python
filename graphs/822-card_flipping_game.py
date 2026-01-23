#822. Card Flipping Game
#Medium
#
#You are given two 0-indexed integer arrays fronts and backs of length n, where
#the ith card has the positive integer fronts[i] printed on the front and
#backs[i] printed on the back. Initially, each card is placed on a table such
#that the front number is facing up.
#
#You may flip any number of cards (possibly zero).
#
#After flipping, the front of each card is facing up. A number is "good" if it
#is facing down on no card (i.e., it is not on the front of any card after flipping).
#
#Return the minimum good number. If there is no good number, return 0.
#
#Example 1:
#Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
#Output: 2
#Explanation: Flip the second card. Now fronts = [1,3,4,4,7], backs = [1,2,4,1,3].
#2 is now good since it's on the back and not on any front.
#
#Example 2:
#Input: fronts = [1], backs = [1]
#Output: 0
#
#Constraints:
#    n == fronts.length == backs.length
#    1 <= n <= 1000
#    1 <= fronts[i], backs[i] <= 2000

class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        """
        A number can never be good if it appears on both sides of the same card.
        Find minimum number that's not on both sides of any card.
        """
        # Numbers that are same on front and back of any card can never be good
        same = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}

        result = float('inf')

        for num in fronts + backs:
            if num not in same:
                result = min(result, num)

        return result if result != float('inf') else 0


class SolutionExplicit:
    """More explicit logic"""

    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        n = len(fronts)

        # Cards where front == back - these numbers can never be hidden
        blocked = set()
        for i in range(n):
            if fronts[i] == backs[i]:
                blocked.add(fronts[i])

        # Find minimum candidate
        min_good = float('inf')

        for i in range(n):
            if fronts[i] not in blocked:
                min_good = min(min_good, fronts[i])
            if backs[i] not in blocked:
                min_good = min(min_good, backs[i])

        return min_good if min_good != float('inf') else 0
