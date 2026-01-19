#374. Guess Number Higher or Lower
#Easy
#
#We are playing the Guess Game. The game is as follows:
#
#I pick a number from 1 to n. You have to guess which number I picked.
#
#Every time you guess wrong, I will tell you whether the number I picked is
#higher or lower than your guess.
#
#You call a pre-defined API int guess(int num), which returns three possible
#results:
#- -1: Your guess is higher than the number I picked (i.e. num > pick).
#- 1: Your guess is lower than the number I picked (i.e. num < pick).
#- 0: your guess is equal to the number I picked (i.e. num == pick).
#
#Return the number that I picked.
#
#Example 1:
#Input: n = 10, pick = 6
#Output: 6
#
#Example 2:
#Input: n = 1, pick = 1
#Output: 1
#
#Example 3:
#Input: n = 2, pick = 1
#Output: 1
#
#Constraints:
#    1 <= n <= 2^31 - 1
#    1 <= pick <= n

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        """Binary search"""
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                # Guess is too high
                right = mid - 1
            else:
                # Guess is too low
                left = mid + 1

        return -1  # Should never reach here


class SolutionRecursive:
    """Recursive binary search"""

    def guessNumber(self, n: int) -> int:
        def binary_search(left, right):
            mid = left + (right - left) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                return binary_search(left, mid - 1)
            else:
                return binary_search(mid + 1, right)

        return binary_search(1, n)


class SolutionTernary:
    """Ternary search (not faster, just different)"""

    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3

            result1 = guess(mid1)
            result2 = guess(mid2)

            if result1 == 0:
                return mid1
            if result2 == 0:
                return mid2

            if result1 == -1:
                right = mid1 - 1
            elif result2 == 1:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1

        return -1
