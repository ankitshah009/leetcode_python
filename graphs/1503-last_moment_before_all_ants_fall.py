#1503. Last Moment Before All Ants Fall Out of a Plank
#Medium
#
#We have a wooden plank of the length n units. Some ants are walking on the plank,
#each ant moves with a speed of 1 unit per second. Some of the ants move to the
#left, the other move to the right.
#
#When two ants moving in different directions meet at some point, they change
#their directions and continue moving again. Assume changing directions does not
#take any additional time.
#
#When an ant reaches one end of the plank at a time t, it falls out of the plank
#immediately.
#
#Given an integer n and two integer arrays left and right, the positions of the
#ants moving to the left and the right, return the moment when the last ant(s)
#fall out of the plank.
#
#Example 1:
#Input: n = 4, left = [4,3], right = [0,1]
#Output: 4
#Explanation: In the image above:
#-The ant at index 0 is named A and going to the right.
#-The ant at index 1 is named B and going to the right.
#-The ant at index 3 is named C and going to the left.
#-The ant at index 4 is named D and going to the left.
#The last moment when an ant was on the plank is t = 4 seconds.
#After that, it falls immediately out of the plank.
#
#Example 2:
#Input: n = 7, left = [], right = [0,1,2,3,4,5,6,7]
#Output: 7
#Explanation: All ants are going to the right, the ant at index 0 needs 7 seconds
#to fall.
#
#Example 3:
#Input: n = 7, left = [0,1,2,3,4,5,6,7], right = []
#Output: 7
#Explanation: All ants are going to the left, the ant at index 7 needs 7 seconds
#to fall.
#
#Constraints:
#    1 <= n <= 10^4
#    0 <= left.length <= n + 1
#    0 <= left[i] <= n
#    0 <= right.length <= n + 1
#    0 <= right[i] <= n
#    1 <= left.length + right.length <= n + 1
#    All values of left and right are unique, and each value can appear only in
#    one of the two arrays.

from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """
        Key insight: when two ants collide and reverse, it's equivalent to
        them passing through each other (they're indistinguishable).

        So we just need to find:
        - Max position among ants going left (time to reach position 0)
        - Max (n - position) among ants going right (time to reach position n)
        """
        time = 0

        # Ants going left: time to fall = position (to reach 0)
        for pos in left:
            time = max(time, pos)

        # Ants going right: time to fall = n - position (to reach n)
        for pos in right:
            time = max(time, n - pos)

        return time


class SolutionOneLiner:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """One-liner solution"""
        return max(
            max(left, default=0),
            max((n - pos for pos in right), default=0)
        )


class SolutionExplained:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """
        Detailed explanation:

        When two ants meet and reverse direction, from the outside it looks
        exactly the same as if they passed through each other.

        Example: Ant A at position 2 going right, Ant B at position 4 going left.
        - They meet at position 3 at time 1
        - After collision: A goes left from 3, B goes right from 3

        This is equivalent to:
        - A continues right and falls at n
        - B continues left and falls at 0

        The time for each ant is independent of collisions!

        Time for ant going left from position p: p seconds
        Time for ant going right from position p: (n - p) seconds
        """
        max_time = 0

        # Left-moving ants
        for pos in left:
            max_time = max(max_time, pos)

        # Right-moving ants
        for pos in right:
            max_time = max(max_time, n - pos)

        return max_time


class SolutionAlternative:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        """Alternative using list comprehension"""
        left_times = [pos for pos in left] if left else [0]
        right_times = [n - pos for pos in right] if right else [0]

        return max(max(left_times), max(right_times))
