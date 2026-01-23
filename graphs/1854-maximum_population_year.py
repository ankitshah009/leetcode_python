#1854. Maximum Population Year
#Easy
#
#You are given a 2D integer array logs where each logs[i] = [birth_i, death_i]
#indicates the birth and death years of the ith person.
#
#The population of some year x is the number of people alive during that year.
#The ith person is counted in year x's population if x is in the inclusive
#range [birth_i, death_i - 1]. Note that the person is not counted in the year
#that they die.
#
#Return the earliest year with the maximum population.
#
#Example 1:
#Input: logs = [[1993,1999],[2000,2010]]
#Output: 1993
#
#Example 2:
#Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
#Output: 1960
#
#Constraints:
#    1 <= logs.length <= 100
#    1950 <= birth_i < death_i <= 2050

from typing import List

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        Line sweep with prefix sum.
        """
        delta = [0] * 101  # Years 1950-2050

        for birth, death in logs:
            delta[birth - 1950] += 1
            delta[death - 1950] -= 1

        max_pop = 0
        result_year = 1950
        current_pop = 0

        for i, d in enumerate(delta):
            current_pop += d
            if current_pop > max_pop:
                max_pop = current_pop
                result_year = 1950 + i

        return result_year


class SolutionBruteForce:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        Check each year.
        """
        max_pop = 0
        result_year = 1950

        for year in range(1950, 2051):
            pop = sum(1 for birth, death in logs if birth <= year < death)
            if pop > max_pop:
                max_pop = pop
                result_year = year

        return result_year


class SolutionEvents:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        Event-based approach.
        """
        events = []

        for birth, death in logs:
            events.append((birth, 1))   # Birth: +1
            events.append((death, -1))  # Death: -1

        events.sort()

        max_pop = 0
        result_year = 1950
        current_pop = 0

        for year, delta in events:
            current_pop += delta
            if current_pop > max_pop:
                max_pop = current_pop
                result_year = year

        return result_year
