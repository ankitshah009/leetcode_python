#1550. Three Consecutive Odds
#Easy
#
#Given an integer array arr, return true if there are three consecutive odd
#numbers in the array. Otherwise, return false.
#
#Example 1:
#Input: arr = [2,6,4,1]
#Output: false
#Explanation: There are no three consecutive odds.
#
#Example 2:
#Input: arr = [1,2,34,3,4,5,7,23,12]
#Output: true
#Explanation: [5,7,23] are three consecutive odds.
#
#Constraints:
#    1 <= arr.length <= 1000
#    1 <= arr[i] <= 1000

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Count consecutive odd numbers.
        """
        count = 0

        for num in arr:
            if num % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0

        return False


class SolutionSliding:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Check every window of size 3.
        """
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False


class SolutionAll:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Using all() for cleaner code.
        """
        for i in range(len(arr) - 2):
            if all(arr[i + j] % 2 == 1 for j in range(3)):
                return True
        return False


class SolutionAny:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Using any() with generator.
        """
        return any(
            arr[i] % 2 == arr[i + 1] % 2 == arr[i + 2] % 2 == 1
            for i in range(len(arr) - 2)
        )


class SolutionBitwise:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Using bitwise AND for odd check.
        """
        for i in range(len(arr) - 2):
            if arr[i] & arr[i + 1] & arr[i + 2] & 1:
                return True
        return False


class SolutionProduct:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Product of three odds is always odd.
        """
        for i in range(len(arr) - 2):
            product = arr[i] * arr[i + 1] * arr[i + 2]
            if product % 2 == 1:
                return True
        return False
