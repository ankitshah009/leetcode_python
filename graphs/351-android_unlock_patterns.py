#351. Android Unlock Patterns
#Medium
#
#Android devices have a special lock screen with a 3 x 3 grid of dots. Users
#can set an "unlock pattern" by connecting the dots in a specific sequence,
#forming a series of joined line segments where each segment's endpoints are
#two consecutive dots in the sequence.
#
#A sequence of k dots is a valid unlock pattern if:
#1. All the dots in the sequence are distinct.
#2. If the line segment connecting two consecutive dots passes through any
#   other dot, the other dot must have previously been in the sequence.
#
#Given two integers m and n, return the number of unique and valid unlock
#patterns of the Android grid lock screen that consist of at least m keys and
#at most n keys.
#
#Example 1:
#Input: m = 1, n = 1
#Output: 9
#
#Example 2:
#Input: m = 1, n = 2
#Output: 65
#
#Constraints:
#    1 <= m, n <= 9

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        """Backtracking with skip map"""
        # skip[i][j] = dot that must be visited before going from i to j
        skip = [[0] * 10 for _ in range(10)]

        # Horizontal
        skip[1][3] = skip[3][1] = 2
        skip[4][6] = skip[6][4] = 5
        skip[7][9] = skip[9][7] = 8

        # Vertical
        skip[1][7] = skip[7][1] = 4
        skip[2][8] = skip[8][2] = 5
        skip[3][9] = skip[9][3] = 6

        # Diagonal
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5

        visited = [False] * 10

        def backtrack(current, remaining):
            if remaining == 0:
                return 1

            visited[current] = True
            count = 0

            for next_dot in range(1, 10):
                # Skip if already visited
                if visited[next_dot]:
                    continue

                # Check if skip dot exists and is visited
                skip_dot = skip[current][next_dot]
                if skip_dot != 0 and not visited[skip_dot]:
                    continue

                count += backtrack(next_dot, remaining - 1)

            visited[current] = False
            return count

        total = 0

        for length in range(m, n + 1):
            # By symmetry:
            # - Starting from corners (1, 3, 7, 9) gives same count
            # - Starting from edges (2, 4, 6, 8) gives same count
            # - Starting from center (5) is unique
            total += backtrack(1, length - 1) * 4  # Corners
            total += backtrack(2, length - 1) * 4  # Edges
            total += backtrack(5, length - 1)      # Center

        return total


class SolutionDetailed:
    """More explicit backtracking"""

    def numberOfPatterns(self, m: int, n: int) -> int:
        def is_valid_move(prev, curr, visited):
            # Direct neighbors (including knights' moves) are always valid
            # Dots that require passing through another dot
            between = {
                (1, 3): 2, (3, 1): 2,
                (4, 6): 5, (6, 4): 5,
                (7, 9): 8, (9, 7): 8,
                (1, 7): 4, (7, 1): 4,
                (2, 8): 5, (8, 2): 5,
                (3, 9): 6, (9, 3): 6,
                (1, 9): 5, (9, 1): 5,
                (3, 7): 5, (7, 3): 5
            }

            if (prev, curr) in between:
                return visited[between[(prev, curr)]]
            return True

        def backtrack(current, visited, length):
            if length == 0:
                return 1

            count = 0
            for next_dot in range(1, 10):
                if not visited[next_dot] and is_valid_move(current, next_dot, visited):
                    visited[next_dot] = True
                    count += backtrack(next_dot, visited, length - 1)
                    visited[next_dot] = False

            return count

        total = 0
        visited = [False] * 10

        for length in range(m, n + 1):
            # Use symmetry
            visited[1] = True
            total += backtrack(1, visited, length - 1) * 4
            visited[1] = False

            visited[2] = True
            total += backtrack(2, visited, length - 1) * 4
            visited[2] = False

            visited[5] = True
            total += backtrack(5, visited, length - 1)
            visited[5] = False

        return total
