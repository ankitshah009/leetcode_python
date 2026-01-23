#1931. Painting a Grid With Three Different Colors
#Hard
#
#You are given two integers m and n. Consider an m x n grid where each cell is
#initially white. You can paint each cell red, green, or blue. All cells must
#be painted.
#
#Return the number of ways to color the grid with no two adjacent cells having
#the same color. Since the answer can be very large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: m = 1, n = 1
#Output: 3
#
#Example 2:
#Input: m = 1, n = 2
#Output: 6
#
#Example 3:
#Input: m = 5, n = 5
#Output: 580986
#
#Constraints:
#    1 <= m <= 5
#    1 <= n <= 1000

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        DP with column states.
        State = coloring of one column (m cells, 3^m possibilities but fewer valid).
        """
        MOD = 10**9 + 7

        def is_valid_column(state: tuple) -> bool:
            """Check if adjacent cells in column have different colors."""
            for i in range(len(state) - 1):
                if state[i] == state[i + 1]:
                    return False
            return True

        def is_compatible(state1: tuple, state2: tuple) -> bool:
            """Check if two adjacent columns are compatible."""
            return all(c1 != c2 for c1, c2 in zip(state1, state2))

        from itertools import product

        # Generate all valid column states
        colors = [0, 1, 2]  # R, G, B
        valid_states = [s for s in product(colors, repeat=m) if is_valid_column(s)]

        # Precompute compatibility
        compatible = {s: [] for s in valid_states}
        for s1 in valid_states:
            for s2 in valid_states:
                if is_compatible(s1, s2):
                    compatible[s1].append(s2)

        # DP: dp[state] = count of ways to reach this state
        dp = {s: 1 for s in valid_states}

        for _ in range(n - 1):
            new_dp = {s: 0 for s in valid_states}
            for state, count in dp.items():
                if count == 0:
                    continue
                for next_state in compatible[state]:
                    new_dp[next_state] = (new_dp[next_state] + count) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD


class SolutionOptimized:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Same approach with matrix exponentiation for large n.
        (Standard DP is efficient enough for n <= 1000)
        """
        MOD = 10**9 + 7

        from itertools import product

        def valid(state):
            return all(state[i] != state[i+1] for i in range(len(state)-1))

        def compatible(s1, s2):
            return all(a != b for a, b in zip(s1, s2))

        states = [s for s in product(range(3), repeat=m) if valid(s)]
        k = len(states)

        # Build transition matrix
        trans = [[0] * k for _ in range(k)]
        for i, s1 in enumerate(states):
            for j, s2 in enumerate(states):
                if compatible(s1, s2):
                    trans[i][j] = 1

        # DP
        dp = [1] * k

        for _ in range(n - 1):
            new_dp = [0] * k
            for i in range(k):
                for j in range(k):
                    if trans[j][i]:
                        new_dp[i] = (new_dp[i] + dp[j]) % MOD
            dp = new_dp

        return sum(dp) % MOD
