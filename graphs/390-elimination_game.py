#390. Elimination Game
#Medium
#
#You have a list arr of all integers in the range [1, n] sorted in a strictly
#increasing order. Apply the following algorithm on arr:
#
#- Starting from left to right, remove the first number and every other number
#  afterward until you reach the end of the list.
#- Repeat the previous step again, but this time from right to left, remove the
#  rightmost number and every other number from the remaining numbers.
#- Keep repeating the steps again, alternating left to right and right to left,
#  until a single number remains.
#
#Given the integer n, return the last number that remains in arr.
#
#Example 1:
#Input: n = 9
#Output: 6
#Explanation:
#arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#arr = [2, 4, 6, 8]
#arr = [2, 6]
#arr = [6]
#
#Example 2:
#Input: n = 1
#Output: 1
#
#Constraints:
#    1 <= n <= 10^9

class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        Mathematical approach - track head position.
        Head changes when:
        - Going left to right (always)
        - Going right to left (if remaining count is odd)
        """
        head = 1
        step = 1
        remaining = n
        left_to_right = True

        while remaining > 1:
            # Update head if going left or going right with odd remaining
            if left_to_right or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head


class SolutionRecursive:
    """
    Recursive approach.
    After one round from left, remaining positions are 2, 4, 6, ...
    Renumber them as 1, 2, 3, ... which is the same problem with n/2.
    But the relationship depends on direction.
    """

    def lastRemaining(self, n: int) -> int:
        def helper(n, left_to_right):
            if n == 1:
                return 1

            if left_to_right:
                # Remaining: 2, 4, 6, ... -> 1, 2, 3, ...
                # f(n, left) = 2 * f(n//2, right)
                return 2 * helper(n // 2, False)
            else:
                # Remaining depends on odd/even
                if n % 2 == 1:
                    # Odd count: same as left
                    return 2 * helper(n // 2, True)
                else:
                    # Even count: 1, 3, 5, ... -> 2*k - 1
                    return 2 * helper(n // 2, True) - 1

        return helper(n, True)


class SolutionSimulation:
    """Simulation (only for small n due to memory)"""

    def lastRemaining(self, n: int) -> int:
        if n <= 100000:  # Only simulate for small n
            arr = list(range(1, n + 1))
            left = True

            while len(arr) > 1:
                if left:
                    arr = arr[1::2]
                else:
                    arr = arr[-2::-2][::-1]
                left = not left

            return arr[0]
        else:
            # Use mathematical solution for large n
            return Solution().lastRemaining(n)
