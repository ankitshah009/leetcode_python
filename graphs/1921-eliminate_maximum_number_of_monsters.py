#1921. Eliminate Maximum Number of Monsters
#Medium
#
#You are playing a video game where you are defending your city from a group of
#n monsters. You are given a 0-indexed integer array dist of size n, where
#dist[i] is the initial distance in kilometers of the ith monster from the
#city.
#
#The monsters walk toward the city at a constant speed. The speed of each
#monster is given to you in an integer array speed of size n, where speed[i] is
#the speed of the ith monster in kilometers per minute.
#
#You have a weapon that, once fully charged, can eliminate a single monster.
#However, the weapon takes one minute to charge. The weapon is fully charged at
#the very start.
#
#You lose when any monster reaches your city. If a monster reaches the city at
#the exact moment the weapon is fully charged, it counts as a loss, and the
#game ends before you can use your weapon.
#
#Return the maximum number of monsters that you can eliminate before you lose,
#or n if you can eliminate all the monsters before any of them reaches the city.
#
#Example 1:
#Input: dist = [1,3,4], speed = [1,1,1]
#Output: 3
#
#Example 2:
#Input: dist = [1,1,2,3], speed = [1,1,1,1]
#Output: 1
#
#Example 3:
#Input: dist = [3,2,4], speed = [5,3,2]
#Output: 1
#
#Constraints:
#    n == dist.length == speed.length
#    1 <= n <= 10^5
#    1 <= dist[i], speed[i] <= 10^5

from typing import List
import math

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        """
        Calculate arrival times, sort, eliminate in order.
        """
        n = len(dist)

        # Time for each monster to reach city
        arrival = [(dist[i] - 1) // speed[i] for i in range(n)]
        # Or equivalently: math.ceil(dist[i] / speed[i]) - 1 gives last safe minute

        arrival.sort()

        for minute, time in enumerate(arrival):
            if time < minute:
                return minute

        return n


class SolutionCeil:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        """
        Using ceiling for arrival time.
        """
        # arrival[i] = time when monster i reaches city
        arrivals = sorted(math.ceil(d / s) for d, s in zip(dist, speed))

        for i, arrival_time in enumerate(arrivals):
            # At minute i, we shoot. Monster arrives at arrival_time.
            # If arrival_time <= i, we lose (monster arrives before or as we shoot)
            if arrival_time <= i:
                return i

        return len(dist)


class SolutionSimple:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        """
        Straightforward approach.
        """
        n = len(dist)
        times = sorted(d / s for d, s in zip(dist, speed))

        for i in range(n):
            if times[i] <= i:
                return i

        return n
