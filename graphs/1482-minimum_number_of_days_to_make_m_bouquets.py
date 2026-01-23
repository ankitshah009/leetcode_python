#1482. Minimum Number of Days to Make m Bouquets
#Medium
#
#You are given an integer array bloomDay, an integer m and an integer k.
#
#You want to make m bouquets. To make a bouquet, you need to use k adjacent
#flowers from the garden.
#
#The garden consists of n flowers, the ith flower will bloom in the bloomDay[i]
#and then can be used in exactly one bouquet.
#
#Return the minimum number of days you need to wait to be able to make m
#bouquets from the garden. If it is impossible to make m bouquets return -1.
#
#Example 1:
#Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
#Output: 3
#Explanation: Let us see what happened in the first three days. x means flower
#bloomed and _ means flower did not bloom in the garden.
#We need 3 bouquets each should contain 1 flower.
#After day 1: [x, _, _, _, _]   // we can only make one bouquet.
#After day 2: [x, _, _, _, x]   // we can only make two bouquets.
#After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
#
#Example 2:
#Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
#Output: -1
#Explanation: We need 3 bouquets each has 2 flowers, that means we need 6
#flowers. We only have 5 flowers so it is impossible to get the needed
#bouquets and we return -1.
#
#Example 3:
#Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
#Output: 12
#Explanation: We need 2 bouquets each should have 3 flowers.
#After day 7: [x, x, x, x, _, x, x]
#We can make one bouquet of the first three flowers that bloomed. We cannot
#make another bouquet from the last three flowers that bloomed because they
#are not adjacent.
#After day 12: [x, x, x, x, x, x, x]
#It is obvious that we can make two bouquets in different ways.
#
#Constraints:
#    bloomDay.length == n
#    1 <= n <= 10^5
#    1 <= bloomDay[i] <= 10^9
#    1 <= m <= 10^6
#    1 <= k <= n

from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Binary search on days.
        For each day, count how many bouquets we can make.
        """
        n = len(bloomDay)

        # Check if possible
        if m * k > n:
            return -1

        def canMakeBouquets(days: int) -> bool:
            """Check if we can make m bouquets by day 'days'"""
            bouquets = 0
            consecutive = 0

            for bloom in bloomDay:
                if bloom <= days:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0

            return bouquets >= m

        # Binary search
        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2

            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1

        return left


class SolutionBinarySearchAlt:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Alternative: binary search on sorted unique days.
        """
        n = len(bloomDay)

        if m * k > n:
            return -1

        def count_bouquets(day: int) -> int:
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            return bouquets

        # Get unique sorted days
        days = sorted(set(bloomDay))

        left, right = 0, len(days) - 1

        while left < right:
            mid = (left + right) // 2

            if count_bouquets(days[mid]) >= m:
                right = mid
            else:
                left = mid + 1

        return days[left]


class SolutionLinear:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Linear approach using events (for comparison).
        Sort by bloom day and process events.
        """
        n = len(bloomDay)

        if m * k > n:
            return -1

        # Create (day, index) pairs and sort by day
        events = sorted((day, i) for i, day in enumerate(bloomDay))

        # Track which flowers have bloomed
        bloomed = [False] * n

        def count_bouquets() -> int:
            bouquets = 0
            consecutive = 0
            for b in bloomed:
                if b:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            return bouquets

        for day, idx in events:
            bloomed[idx] = True
            if count_bouquets() >= m:
                return day

        return max(bloomDay)
