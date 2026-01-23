#672. Bulb Switcher II
#Medium
#
#There is a room with n bulbs labeled from 1 to n that all are turned on initially,
#and four buttons on the wall. Each of the four buttons has a different functionality:
#
#- Button 1: Flips the status of all the bulbs.
#- Button 2: Flips the status of all the bulbs with even labels.
#- Button 3: Flips the status of all the bulbs with odd labels.
#- Button 4: Flips the status of all the bulbs with label j = 3k + 1 (k = 0, 1, 2, ...)
#
#Given two integers n and presses, return the number of different possible statuses
#after performing all presses button presses.
#
#Example 1:
#Input: n = 1, presses = 1
#Output: 2
#
#Example 2:
#Input: n = 2, presses = 1
#Output: 3
#
#Example 3:
#Input: n = 3, presses = 1
#Output: 4
#
#Constraints:
#    1 <= n <= 1000
#    0 <= presses <= 1000

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        """
        Key insight: Pattern repeats every 3 bulbs!
        Only first 3 bulbs matter. Also, pressing same button twice cancels out.

        The operations have period 6 (LCM of 1, 2, 3):
        - Op1: affects all bulbs
        - Op2: affects even bulbs
        - Op3: affects odd bulbs
        - Op4: affects 1, 4, 7, ... (1-indexed)

        For first 3 bulbs (1-indexed: 1, 2, 3):
        - Op1: flip all -> 111
        - Op2: flip 2   -> 010
        - Op3: flip 1,3 -> 101
        - Op4: flip 1   -> 100

        Note: Op1 = Op2 XOR Op3, so only 3 independent operations.
        """
        # Reduce n to effective size (only first 3 matter)
        n = min(n, 3)

        if presses == 0:
            return 1

        if n == 1:
            # Only bulb 1, can be on or off
            return 2

        if n == 2:
            # Bulbs 1 and 2
            if presses == 1:
                return 3  # 00, 01, 10 (can't get 11 without affecting both)
            return 4  # All 4 states possible with 2+ presses

        # n >= 3
        if presses == 1:
            return 4  # Each single button press gives unique state
        if presses == 2:
            return 7  # Can achieve 7 different states
        return 8  # All 8 states possible with 3+ presses


class SolutionBruteForce:
    """Brute force with memoization for verification"""

    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1

        n = min(n, 3)

        # All bulbs start ON (1)
        initial = (1 << n) - 1

        # Define operations for first n bulbs
        def flip_all(state):
            return state ^ ((1 << n) - 1)

        def flip_even(state):
            mask = 0
            for i in range(2, n + 1, 2):
                mask |= (1 << (i - 1))
            return state ^ mask

        def flip_odd(state):
            mask = 0
            for i in range(1, n + 1, 2):
                mask |= (1 << (i - 1))
            return state ^ mask

        def flip_3k1(state):
            mask = 0
            for i in range(1, n + 1, 3):
                mask |= (1 << (i - 1))
            return state ^ mask

        ops = [flip_all, flip_even, flip_odd, flip_3k1]

        # BFS to find all reachable states
        current = {initial}

        for _ in range(presses):
            next_states = set()
            for state in current:
                for op in ops:
                    next_states.add(op(state))
            current = next_states

        return len(current)
