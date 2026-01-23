#1109. Corporate Flight Bookings
#Medium
#
#There are n flights that are labeled from 1 to n.
#
#You are given an array of flight bookings bookings, where bookings[i] =
#[firsti, lasti, seatsi] represents a booking for flights firsti through
#lasti (inclusive) with seatsi seats reserved for each flight in the range.
#
#Return an array answer of length n, where answer[i] is the total number
#of seats reserved for flight i.
#
#Example 1:
#Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
#Output: [10,55,45,25,25]
#Explanation:
#Flight labels:        1   2   3   4   5
#Booking 1 reserved:  10  10
#Booking 2 reserved:      20  20
#Booking 3 reserved:      25  25  25  25
#Total seats:         10  55  45  25  25
#
#Example 2:
#Input: bookings = [[1,2,10],[2,2,15]], n = 2
#Output: [10,25]
#
#Constraints:
#    1 <= n <= 2 * 10^4
#    1 <= bookings.length <= 2 * 10^4
#    bookings[i].length == 3
#    1 <= firsti <= lasti <= n
#    1 <= seatsi <= 10^4

from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        Difference array / sweep line.
        Add seats at start, subtract at end+1.
        """
        diff = [0] * (n + 1)

        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        # Compute prefix sum
        result = [0] * n
        result[0] = diff[0]
        for i in range(1, n):
            result[i] = result[i - 1] + diff[i]

        return result


class SolutionInPlace:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """In-place difference array"""
        result = [0] * (n + 1)

        for first, last, seats in bookings:
            result[first - 1] += seats
            result[last] -= seats

        for i in range(1, n):
            result[i] += result[i - 1]

        return result[:-1]


class SolutionBruteForce:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """O(n * bookings) brute force"""
        result = [0] * n

        for first, last, seats in bookings:
            for i in range(first - 1, last):
                result[i] += seats

        return result
