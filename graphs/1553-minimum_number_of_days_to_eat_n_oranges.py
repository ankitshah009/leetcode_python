#1553. Minimum Number of Days to Eat N Oranges
#Hard
#
#There are n oranges in the kitchen and you decided to eat some of these oranges
#every day as follows:
#- Eat one orange.
#- If the number of remaining oranges n is divisible by 2 then you can eat n / 2
#  oranges.
#- If the number of remaining oranges n is divisible by 3 then you can eat
#  2 * (n / 3) oranges.
#
#You can only choose one of the actions per day.
#
#Given the integer n, return the minimum number of days to eat n oranges.
#
#Example 1:
#Input: n = 10
#Output: 4
#Explanation: You have 10 oranges.
#Day 1: Eat 1 orange, 10 - 1 = 9.
#Day 2: Eat 6 oranges, 9 - 6 = 3. (Since 9 is divisible by 3)
#Day 3: Eat 2 oranges, 3 - 2 = 1.
#Day 4: Eat 1 orange, 1 - 1 = 0.
#
#Example 2:
#Input: n = 6
#Output: 3
#Explanation: You have 6 oranges.
#Day 1: Eat 3 oranges, 6 - 3 = 3. (Since 6 is divisible by 2)
#Day 2: Eat 2 oranges, 3 - 2 = 1.
#Day 3: Eat 1 orange, 1 - 1 = 0.
#
#Constraints:
#    1 <= n <= 2 * 10^9

from functools import lru_cache

class Solution:
    def minDays(self, n: int) -> int:
        """
        Key insight: Eating one orange at a time is rarely optimal.
        It's better to eat 1's to get to a divisible number, then divide.

        Use memoization with only divisible transitions.
        """
        @lru_cache(maxsize=None)
        def dp(oranges: int) -> int:
            if oranges <= 1:
                return oranges

            # Option 1: Reduce to make divisible by 2, then divide
            # Need (oranges % 2) days to eat ones, then 1 day to eat half
            option1 = (oranges % 2) + 1 + dp(oranges // 2)

            # Option 2: Reduce to make divisible by 3, then divide
            # Need (oranges % 3) days to eat ones, then 1 day to eat 2/3
            option2 = (oranges % 3) + 1 + dp(oranges // 3)

            return min(option1, option2)

        return dp(n)


class SolutionBFS:
    def minDays(self, n: int) -> int:
        """
        BFS approach (less efficient but works for smaller n).
        """
        from collections import deque

        if n <= 1:
            return n

        queue = deque([(n, 0)])
        visited = {n}

        while queue:
            oranges, days = queue.popleft()

            # Try eating one
            next_states = [oranges - 1]

            # Try eating half
            if oranges % 2 == 0:
                next_states.append(oranges // 2)

            # Try eating 2/3
            if oranges % 3 == 0:
                next_states.append(oranges // 3)

            for next_n in next_states:
                if next_n == 0:
                    return days + 1
                if next_n not in visited:
                    visited.add(next_n)
                    queue.append((next_n, days + 1))

        return -1


class SolutionOptimized:
    def minDays(self, n: int) -> int:
        """
        Optimized BFS: Only consider states reachable by eating to
        divisibility and then dividing.
        """
        from collections import deque

        if n <= 1:
            return n

        # States: (remaining oranges, days)
        queue = deque([(n, 0)])
        visited = {n}

        while queue:
            curr, days = queue.popleft()

            if curr == 0:
                return days

            # Generate next meaningful states
            next_states = []

            # Eat down to multiple of 2, then halve
            if curr >= 2:
                remainder = curr % 2
                next_n = curr // 2
                next_states.append((next_n, days + remainder + 1))

            # Eat down to multiple of 3, then take 1/3
            if curr >= 3:
                remainder = curr % 3
                next_n = curr // 3
                next_states.append((next_n, days + remainder + 1))

            # Just eat one (only needed for small numbers)
            if curr <= 2:
                next_states.append((curr - 1, days + 1))

            for next_n, next_days in next_states:
                if next_n not in visited:
                    visited.add(next_n)
                    queue.append((next_n, next_days))

        return -1


class SolutionMemo:
    def minDays(self, n: int) -> int:
        """
        Explicit memoization with dictionary.
        """
        memo = {}

        def solve(oranges):
            if oranges <= 1:
                return oranges

            if oranges in memo:
                return memo[oranges]

            # Always use division strategies
            result = min(
                oranges % 2 + 1 + solve(oranges // 2),
                oranges % 3 + 1 + solve(oranges // 3)
            )

            memo[oranges] = result
            return result

        return solve(n)
