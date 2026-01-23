#1011. Capacity To Ship Packages Within D Days
#Medium
#
#A conveyor belt has packages that must be shipped from one port to another
#within days days.
#
#The i-th package on the conveyor belt has a weight of weights[i]. Each day, we
#load the ship with packages on the conveyor belt (in the order given by
#weights). We may not load more weight than the maximum weight capacity of the
#ship.
#
#Return the least weight capacity of the ship that will result in all the
#packages on the conveyor belt being shipped within days days.
#
#Example 1:
#Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
#Output: 15
#Explanation: Ship with capacity 15: [1,2,3,4,5], [6,7], [8], [9], [10]
#
#Example 2:
#Input: weights = [3,2,2,4,1,4], days = 3
#Output: 6
#
#Example 3:
#Input: weights = [1,2,3,1,1], days = 4
#Output: 3
#
#Constraints:
#    1 <= days <= weights.length <= 5 * 10^4
#    1 <= weights[i] <= 500

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Binary search on capacity.
        """
        def can_ship(capacity):
            days_needed = 1
            current_load = 0

            for w in weights:
                if current_load + w > capacity:
                    days_needed += 1
                    current_load = w
                else:
                    current_load += w

            return days_needed <= days

        left = max(weights)  # Must carry heaviest package
        right = sum(weights)  # Worst case: all in one day

        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left


class SolutionExplicit:
    """More explicit binary search"""

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def days_needed(capacity):
            count = 1
            load = 0

            for w in weights:
                if load + w > capacity:
                    count += 1
                    load = w
                else:
                    load += w

            return count

        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            if days_needed(mid) <= days:
                hi = mid
            else:
                lo = mid + 1

        return lo
