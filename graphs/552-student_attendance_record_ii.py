#552. Student Attendance Record II
#Hard
#
#An attendance record for a student can be represented as a string where each
#character signifies whether the student was absent, late, or present on that day.
#- 'A': Absent.
#- 'L': Late.
#- 'P': Present.
#
#A student is eligible for an attendance award if they meet both criteria:
#- The student was absent ('A') for strictly fewer than 2 days total.
#- The student was never late ('L') for 3 or more consecutive days.
#
#Given an integer n, return the number of possible attendance records of length n
#that make a student eligible for an attendance award. The answer may be very large,
#so return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 2
#Output: 8
#Explanation: There are 8 records with length 2 that are eligible:
#"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
#
#Example 2:
#Input: n = 1
#Output: 3
#
#Example 3:
#Input: n = 10101
#Output: 183236316
#
#Constraints:
#    1 <= n <= 10^5

class Solution:
    def checkRecord(self, n: int) -> int:
        """
        DP with states: (total_absences, consecutive_lates)
        dp[i][j][k] = records of length i with j absences and k consecutive lates at end
        """
        MOD = 10**9 + 7

        # dp[j][k] = count with j absences (0 or 1), k consecutive lates (0, 1, or 2)
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1  # Empty record

        for _ in range(n):
            new_dp = [[0] * 3 for _ in range(2)]

            for j in range(2):  # Absences
                for k in range(3):  # Consecutive lates
                    if dp[j][k] == 0:
                        continue

                    # Add 'P' - resets late streak
                    new_dp[j][0] = (new_dp[j][0] + dp[j][k]) % MOD

                    # Add 'A' - if we haven't used absence yet
                    if j == 0:
                        new_dp[1][0] = (new_dp[1][0] + dp[j][k]) % MOD

                    # Add 'L' - if streak < 2
                    if k < 2:
                        new_dp[j][k + 1] = (new_dp[j][k + 1] + dp[j][k]) % MOD

            dp = new_dp

        # Sum all valid states
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[j][k]) % MOD

        return result


class SolutionMatrix:
    """Matrix exponentiation for O(log n) time"""

    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # State: (0A,0L), (0A,1L), (0A,2L), (1A,0L), (1A,1L), (1A,2L)
        # Transition matrix
        M = [
            [1, 1, 1, 0, 0, 0],  # P from any 0A state
            [1, 0, 0, 0, 0, 0],  # L from (0A,0L)
            [0, 1, 0, 0, 0, 0],  # L from (0A,1L)
            [1, 1, 1, 1, 1, 1],  # A from any 0A state, P from any 1A state
            [0, 0, 0, 1, 0, 0],  # L from (1A,0L)
            [0, 0, 0, 0, 1, 0],  # L from (1A,1L)
        ]

        def multiply(A, B):
            size = len(A)
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        def matrix_pow(mat, p):
            size = len(mat)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
            while p:
                if p & 1:
                    result = multiply(result, mat)
                mat = multiply(mat, mat)
                p >>= 1
            return result

        result_matrix = matrix_pow(M, n)
        return sum(result_matrix[i][0] for i in range(6)) % MOD
