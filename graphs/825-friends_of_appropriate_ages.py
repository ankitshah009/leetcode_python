#825. Friends Of Appropriate Ages
#Medium
#
#There are n persons on a social media website. You are given an integer array
#ages where ages[i] is the age of the ith person.
#
#Person x will not send a friend request to person y (x != y) if any of the
#following conditions is true:
#- age[y] <= 0.5 * age[x] + 7
#- age[y] > age[x]
#- age[y] > 100 && age[x] < 100
#
#Otherwise, x will send a friend request to y.
#
#Note that if x sends a request to y, y will not necessarily send a request to x.
#Also, a person will not send a friend request to themselves.
#
#Return the total number of friend requests made.
#
#Example 1:
#Input: ages = [16,16]
#Output: 2
#Explanation: 2 people friend request each other.
#
#Example 2:
#Input: ages = [16,17,18]
#Output: 2
#
#Example 3:
#Input: ages = [20,30,100,110,120]
#Output: 3
#
#Constraints:
#    n == ages.length
#    1 <= n <= 2 * 10^4
#    1 <= ages[i] <= 120

from collections import Counter

class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        """
        Count by age since ages are limited to 1-120.
        x sends to y if: 0.5*x + 7 < y <= x (and y > 100 condition is redundant when y <= x)
        """
        age_count = Counter(ages)
        total = 0

        for age_x, count_x in age_count.items():
            for age_y, count_y in age_count.items():
                # Check conditions
                if age_y <= 0.5 * age_x + 7:
                    continue
                if age_y > age_x:
                    continue
                if age_y > 100 and age_x < 100:
                    continue

                # Valid friend request
                if age_x == age_y:
                    # Same age: count_x * (count_x - 1) requests
                    total += count_x * (count_x - 1)
                else:
                    total += count_x * count_y

        return total


class SolutionBinarySearch:
    """Binary search approach"""

    def numFriendRequests(self, ages: list[int]) -> int:
        from bisect import bisect_left, bisect_right

        ages.sort()
        n = len(ages)
        total = 0

        for i, age in enumerate(ages):
            # y must satisfy: 0.5*age + 7 < y <= age
            low = 0.5 * age + 7
            high = age

            if low >= high:
                continue

            # Count people in range (low, high]
            left = bisect_right(ages, low)
            right = bisect_right(ages, high)

            count = right - left

            # Subtract self
            if left <= i < right:
                count -= 1

            total += count

        return total


class SolutionPrefixSum:
    """Using prefix sum on age counts"""

    def numFriendRequests(self, ages: list[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        # Prefix sum for counting
        prefix = [0] * 122
        for i in range(1, 121):
            prefix[i + 1] = prefix[i] + count[i]

        total = 0
        for age in range(1, 121):
            if count[age] == 0:
                continue

            # Valid y range: (0.5*age + 7, age]
            low = int(0.5 * age + 7)
            if low >= age:
                continue

            # Count in range (low, age]
            valid_count = prefix[age + 1] - prefix[low + 1]

            # Each person of this age sends to valid_count - 1 (excluding self)
            total += count[age] * (valid_count - 1)

        return total
