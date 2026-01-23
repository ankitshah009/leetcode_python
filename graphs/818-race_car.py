#818. Race Car
#Hard
#
#Your car starts at position 0 and speed +1 on an infinite number line. Your
#car can go into negative positions. Your car drives automatically according
#to a sequence of instructions 'A' (accelerate) and 'R' (reverse):
#
#When you get an instruction 'A', your car does the following:
#- position += speed
#- speed *= 2
#
#When you get an instruction 'R', your car does the following:
#- If your speed is positive then speed = -1
#- otherwise speed = 1
#Your position stays the same.
#
#Given a target position target, return the length of the shortest sequence of
#instructions to get there.
#
#Example 1:
#Input: target = 3
#Output: 2
#Explanation: "AA" - 0 -> 1 -> 3 (position), 1 -> 2 -> 4 (speed)
#
#Example 2:
#Input: target = 6
#Output: 5
#Explanation: "AAARA" - 0 -> 1 -> 3 -> 7 -> 7 -> 6
#
#Constraints:
#    1 <= target <= 10^4

from collections import deque
from functools import lru_cache

class Solution:
    def racecar(self, target: int) -> int:
        """
        DP approach: find optimal way to reach each position.
        """
        @lru_cache(maxsize=None)
        def dp(t):
            # Find n where 2^n - 1 >= t
            n = t.bit_length()
            if (1 << n) - 1 == t:
                return n  # Exactly reachable with n A's

            # Option 1: Go past target with n A's, then reverse
            # Position after n A's: 2^n - 1
            result = n + 1 + dp((1 << n) - 1 - t)

            # Option 2: Go (n-1) A's, reverse, go back some, reverse, continue
            # Position after (n-1) A's: 2^(n-1) - 1
            for m in range(n - 1):
                # After n-1 A's: position = 2^(n-1) - 1
                # Reverse, do m A's backwards: position = 2^(n-1) - 1 - (2^m - 1)
                # Reverse again, continue towards target
                pos = (1 << (n - 1)) - 1 - ((1 << m) - 1)
                result = min(result, (n - 1) + 1 + m + 1 + dp(t - pos))

            return result

        return dp(target)


class SolutionBFS:
    """BFS on (position, speed) states"""

    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])  # (position, speed, steps)
        visited = {(0, 1)}

        while queue:
            pos, speed, steps = queue.popleft()

            if pos == target:
                return steps

            # Accelerate
            new_pos = pos + speed
            new_speed = speed * 2
            if (new_pos, new_speed) not in visited and 0 < new_pos < 2 * target:
                visited.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, steps + 1))

            # Reverse
            new_speed = -1 if speed > 0 else 1
            if (pos, new_speed) not in visited:
                visited.add((pos, new_speed))
                queue.append((pos, new_speed, steps + 1))

        return -1


class SolutionDP:
    """Bottom-up DP"""

    def racecar(self, target: int) -> int:
        dp = [float('inf')] * (target + 1)
        dp[0] = 0

        for t in range(1, target + 1):
            n = t.bit_length()

            # Exact match
            if (1 << n) - 1 == t:
                dp[t] = n
                continue

            # Overshoot and return
            dp[t] = n + 1 + dp[(1 << n) - 1 - t]

            # Undershoot, reverse, go back, reverse, continue
            for m in range(n - 1):
                pos = (1 << (n - 1)) - 1 - ((1 << m) - 1)
                if t - pos >= 0:
                    dp[t] = min(dp[t], (n - 1) + 1 + m + 1 + dp[t - pos])

        return dp[target]
