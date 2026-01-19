#397. Integer Replacement
#Medium
#
#Given a positive integer n, you can apply one of the following operations:
#
#1. If n is even, replace n with n / 2.
#2. If n is odd, replace n with either n + 1 or n - 1.
#
#Return the minimum number of operations needed for n to become 1.
#
#Example 1:
#Input: n = 8
#Output: 3
#Explanation: 8 -> 4 -> 2 -> 1
#
#Example 2:
#Input: n = 7
#Output: 4
#Explanation: 7 -> 8 -> 4 -> 2 -> 1
#or 7 -> 6 -> 3 -> 2 -> 1
#
#Example 3:
#Input: n = 4
#Output: 2
#
#Constraints:
#    1 <= n <= 2^31 - 1

from functools import lru_cache

class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        Bit manipulation insight:
        - If even: divide by 2
        - If odd:
          - If n = 3 or last two bits are 01: subtract 1
          - Otherwise (last two bits are 11): add 1
        This greedy approach creates more trailing zeros.
        """
        count = 0

        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or (n & 3) == 1:
                # n % 4 == 1 or n == 3
                n -= 1
            else:
                # n % 4 == 3
                n += 1
            count += 1

        return count


class SolutionMemo:
    """Memoization approach"""

    def integerReplacement(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dp(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return 1 + dp(num // 2)
            return 1 + min(dp(num + 1), dp(num - 1))

        return dp(n)


class SolutionBFS:
    """BFS for shortest path"""

    def integerReplacement(self, n: int) -> int:
        from collections import deque

        queue = deque([(n, 0)])
        visited = {n}

        while queue:
            num, steps = queue.popleft()

            if num == 1:
                return steps

            if num % 2 == 0:
                next_num = num // 2
                if next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, steps + 1))
            else:
                for next_num in [num + 1, num - 1]:
                    if next_num not in visited:
                        visited.add(next_num)
                        queue.append((next_num, steps + 1))

        return -1


class SolutionBits:
    """Pure bit manipulation"""

    def integerReplacement(self, n: int) -> int:
        count = 0

        while n != 1:
            if n & 1 == 0:
                # Even
                n >>= 1
            elif n == 3 or (n >> 1) & 1 == 0:
                # Odd and (n is 3 or next bit is 0)
                n -= 1
            else:
                # Odd and next bit is 1
                n += 1
            count += 1

        return count
