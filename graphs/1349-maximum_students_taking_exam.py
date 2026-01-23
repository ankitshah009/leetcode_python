#1349. Maximum Students Taking Exam
#Hard
#
#Given a m * n matrix seats that represent seats distributions in a classroom.
#If a seat is broken, it is denoted by '#' character otherwise it is denoted
#by a '.' character.
#
#Students can see the answers of those sitting next to the left, right, upper
#left and upper right, but he cannot see the answers of the student sitting
#directly in front or behind him. Return the maximum number of students that
#can take the exam together without any cheating being possible.
#
#Students must be placed in seats in good condition.
#
#Example 1:
#Input: seats = [["#",".","#","#",".","#"],
#                [".","#","#","#","#","."],
#                ["#",".","#","#",".","#"]]
#Output: 4
#Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam.
#
#Example 2:
#Input: seats = [[".","#"],
#                ["#","#"],
#                ["#","."],
#                ["#","#"],
#                [".","#"]]
#Output: 3
#
#Example 3:
#Input: seats = [["#",".",".",".","#"],
#                [".","#",".","#","."],
#                [".",".","#",".","."],
#                [".","#",".","#","."],
#                ["#",".",".",".","#"]]
#Output: 10
#
#Constraints:
#    seats contains only characters '.' and '#'.
#    m == seats.length
#    n == seats[i].length
#    1 <= m <= 8
#    1 <= n <= 8

from typing import List
from functools import lru_cache

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        """
        Bitmask DP: dp[row][mask] = max students for rows 0..row with mask for current row.
        mask represents which seats in the row have students.
        """
        m, n = len(seats), len(seats[0])

        # Convert seats to valid masks (1 where seat is available)
        valid = []
        for row in seats:
            mask = 0
            for j, seat in enumerate(row):
                if seat == '.':
                    mask |= (1 << j)
            valid.append(mask)

        @lru_cache(maxsize=None)
        def dp(row, prev_mask):
            if row == m:
                return 0

            max_students = 0

            # Try all possible arrangements for current row
            for mask in range(1 << n):
                # Check if valid:
                # 1. Only use available seats
                if mask & ~valid[row]:
                    continue

                # 2. No adjacent students in same row
                if mask & (mask >> 1):
                    continue

                # 3. No upper-left or upper-right visibility from prev row
                if row > 0:
                    if mask & (prev_mask >> 1):  # Upper right
                        continue
                    if mask & (prev_mask << 1):  # Upper left
                        continue

                students = bin(mask).count('1')
                max_students = max(max_students, students + dp(row + 1, mask))

            return max_students

        return dp(0, 0)


class SolutionBottomUp:
    def maxStudents(self, seats: List[List[str]]) -> int:
        """Bottom-up bitmask DP"""
        m, n = len(seats), len(seats[0])

        # Valid seat masks for each row
        valid = []
        for row in seats:
            mask = 0
            for j, seat in enumerate(row):
                if seat == '.':
                    mask |= (1 << j)
            valid.append(mask)

        # dp[mask] = max students achievable with current row having 'mask' arrangement
        prev_dp = {0: 0}

        for row in range(m):
            curr_dp = {}

            for mask in range(1 << n):
                # Check valid arrangement
                if mask & ~valid[row]:
                    continue
                if mask & (mask >> 1):
                    continue

                students = bin(mask).count('1')

                for prev_mask, prev_count in prev_dp.items():
                    # Check no cheating from previous row
                    if mask & (prev_mask >> 1):  # Upper right
                        continue
                    if mask & (prev_mask << 1):  # Upper left
                        continue

                    total = prev_count + students
                    if mask not in curr_dp or curr_dp[mask] < total:
                        curr_dp[mask] = total

            prev_dp = curr_dp if curr_dp else {0: 0}

        return max(prev_dp.values()) if prev_dp else 0
