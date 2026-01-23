#1052. Grumpy Bookstore Owner
#Medium
#
#There is a bookstore owner that has a store open for n minutes. Every minute,
#some number of customers enter the store. You are given an integer array
#customers of length n where customers[i] is the number of customers that
#enter the store at the start of the ith minute and all those customers
#leave after the end of that minute.
#
#On some minutes, the bookstore owner is grumpy. You are given a binary array
#grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith
#minute, and is 0 otherwise.
#
#When the bookstore owner is grumpy, the customers of that minute are not
#satisfied, otherwise they are satisfied.
#
#The bookstore owner knows a secret technique to keep themselves not grumpy
#for minutes consecutive minutes, but can only use it once.
#
#Return the maximum number of customers that can be satisfied throughout the day.
#
#Example 1:
#Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
#Output: 16
#Explanation: The bookstore owner keeps themselves not grumpy for the last 3
#minutes. Maximum customers satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
#
#Example 2:
#Input: customers = [1], grumpy = [0], minutes = 1
#Output: 1
#
#Constraints:
#    n == customers.length == grumpy.length
#    1 <= minutes <= n <= 2 * 10^4
#    0 <= customers[i] <= 1000
#    grumpy[i] is either 0 or 1.

from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        Sliding window to find best window for secret technique.

        Base satisfied = customers when not grumpy
        Find window that saves most customers (when grumpy)
        """
        n = len(customers)

        # Base satisfied customers (when owner is not grumpy)
        base = sum(c for c, g in zip(customers, grumpy) if g == 0)

        # Find window that saves most grumpy customers
        # Initial window
        saved = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_saved = saved

        # Slide window
        for i in range(minutes, n):
            # Add right
            if grumpy[i] == 1:
                saved += customers[i]
            # Remove left
            if grumpy[i - minutes] == 1:
                saved -= customers[i - minutes]

            max_saved = max(max_saved, saved)

        return base + max_saved


class SolutionAlternative:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """Track extra satisfied in window"""
        n = len(customers)

        # Always satisfied
        always = sum(c * (1 - g) for c, g in zip(customers, grumpy))

        # Extra we can save with technique
        extra = sum(customers[i] * grumpy[i] for i in range(minutes))
        max_extra = extra

        for i in range(minutes, n):
            extra += customers[i] * grumpy[i]
            extra -= customers[i - minutes] * grumpy[i - minutes]
            max_extra = max(max_extra, extra)

        return always + max_extra
