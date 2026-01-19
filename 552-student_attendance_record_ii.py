#552. Student Attendance Record II
#Hard
#
#An attendance record for a student can be represented as a string where each character
#signifies whether the student was absent, late, or present on that day. The record only
#contains the following three characters:
#    'A': Absent.
#    'L': Late.
#    'P': Present.
#
#Any student is eligible for an attendance award if they meet both of the following criteria:
#    The student was absent ('A') for strictly fewer than 2 days total.
#    The student was never late ('L') for 3 or more consecutive days.
#
#Given an integer n, return the number of possible attendance records of length n that make
#a student eligible for an attendance award. The answer may be very large, so return it
#modulo 10^9 + 7.
#
#Example 1:
#Input: n = 2
#Output: 8
#Explanation: There are 8 records with length 2 that are eligible for an award:
#"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
#Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
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
        MOD = 10**9 + 7

        # dp[i][j][k] = number of valid sequences of length i
        # j = number of 'A's (0 or 1)
        # k = number of consecutive 'L's at the end (0, 1, or 2)

        # Space optimized: only need previous state
        # State: [absent_count][consecutive_late_count]
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1  # Empty sequence

        for _ in range(n):
            new_dp = [[0] * 3 for _ in range(2)]

            for absent in range(2):
                for late in range(3):
                    if dp[absent][late] == 0:
                        continue

                    # Add 'P': resets consecutive lates
                    new_dp[absent][0] = (new_dp[absent][0] + dp[absent][late]) % MOD

                    # Add 'A': only if no absences yet
                    if absent == 0:
                        new_dp[1][0] = (new_dp[1][0] + dp[absent][late]) % MOD

                    # Add 'L': only if < 2 consecutive lates
                    if late < 2:
                        new_dp[absent][late + 1] = (new_dp[absent][late + 1] + dp[absent][late]) % MOD

            dp = new_dp

        # Sum all valid ending states
        result = 0
        for absent in range(2):
            for late in range(3):
                result = (result + dp[absent][late]) % MOD

        return result
