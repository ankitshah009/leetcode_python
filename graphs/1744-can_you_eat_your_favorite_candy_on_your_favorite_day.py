#1744. Can You Eat Your Favorite Candy on Your Favorite Day?
#Medium
#
#You are given a (0-indexed) array of positive integers candiesCount where
#candiesCount[i] represents the number of candies of the ith type you have. You
#are also given a 2D array queries where queries[i] = [favoriteTypei, favoriteDayi,
#dailyCapi].
#
#You play a game with the following rules:
#- You start eating candies on day 0.
#- You cannot eat any candy of type i unless you have eaten all candies of type
#  i - 1.
#- You must eat at least one candy per day until you have eaten all the candies.
#
#Construct a boolean array answer such that answer.length == queries.length and
#answer[i] is true if you can eat a candy of type favoriteTypei on day favoriteDayi
#without eating more than dailyCapi candies on any day, and false otherwise.
#
#Example 1:
#Input: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
#Output: [true,false,true]
#
#Constraints:
#    1 <= candiesCount.length <= 10^5
#    1 <= candiesCount[i] <= 10^5
#    1 <= queries.length <= 10^5
#    queries[i].length == 3
#    0 <= favoriteTypei < candiesCount.length
#    0 <= favoriteDayi <= 10^9
#    1 <= dailyCapi <= 10^9

from typing import List

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        """
        Prefix sum to determine range of days when we can eat type i.

        To eat candy of type i on day d:
        - We must have eaten at most (d+1) * cap candies by day d
        - We must have eaten at least prefix[i] + 1 candies by day d

        So we need: prefix[i] < (d + 1) * cap  AND  prefix[i+1] > d
        """
        n = len(candiesCount)

        # Prefix sum: prefix[i] = total candies of types 0 to i-1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + candiesCount[i]

        result = []

        for fav_type, fav_day, daily_cap in queries:
            # Minimum candies we must eat before reaching type fav_type
            min_candies_before = prefix[fav_type]

            # Maximum candies we could have eaten by fav_day
            max_candies_by_day = (fav_day + 1) * daily_cap

            # Minimum candies we could have eaten by fav_day (at least 1 per day)
            min_candies_by_day = fav_day + 1

            # Total candies of types 0 to fav_type
            total_candies_through_type = prefix[fav_type + 1]

            # Check if we can eat candy of fav_type on fav_day
            # 1. We must be able to reach type fav_type: min_candies_before < max_candies_by_day
            # 2. Type fav_type must not be finished: total_candies_through_type >= min_candies_by_day

            can_reach = min_candies_before < max_candies_by_day
            not_finished = total_candies_through_type >= min_candies_by_day

            result.append(can_reach and not_finished)

        return result


class SolutionDetailed:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        """
        Same logic with detailed comments.
        """
        # Build prefix sum
        prefix = [0]
        for count in candiesCount:
            prefix.append(prefix[-1] + count)

        result = []

        for fav_type, fav_day, cap in queries:
            # Day fav_day means we've had fav_day+1 days (0-indexed)
            days = fav_day + 1

            # Range of candies we could have eaten by end of fav_day:
            # Min: eat 1 per day = days
            # Max: eat cap per day = days * cap

            # Range of candy indices that are type fav_type:
            # From prefix[fav_type] + 1 to prefix[fav_type + 1]

            min_eaten = days
            max_eaten = days * cap
            type_start = prefix[fav_type] + 1
            type_end = prefix[fav_type + 1]

            # Intervals must overlap
            # [min_eaten, max_eaten] overlaps with [type_start, type_end]
            overlap = min_eaten <= type_end and max_eaten >= type_start

            result.append(overlap)

        return result
