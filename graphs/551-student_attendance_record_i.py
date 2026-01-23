#551. Student Attendance Record I
#Easy
#
#You are given a string s representing an attendance record for a student where
#each character signifies whether the student was absent, late, or present on that day.
#- 'A': Absent.
#- 'L': Late.
#- 'P': Present.
#
#The student is eligible for an attendance award if they meet both of the following:
#- The student was absent ('A') for strictly fewer than 2 days total.
#- The student was never late ('L') for 3 or more consecutive days.
#
#Return true if the student is eligible for an attendance award, or false otherwise.
#
#Example 1:
#Input: s = "PPALLP"
#Output: true
#
#Example 2:
#Input: s = "PPALLL"
#Output: false
#
#Constraints:
#    1 <= s.length <= 1000
#    s[i] is either 'A', 'L', or 'P'.

class Solution:
    def checkRecord(self, s: str) -> bool:
        """Check both conditions"""
        return s.count('A') < 2 and 'LLL' not in s


class SolutionExplicit:
    """Explicit iteration"""

    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_streak = 0

        for c in s:
            if c == 'A':
                absent_count += 1
                late_streak = 0
                if absent_count >= 2:
                    return False
            elif c == 'L':
                late_streak += 1
                if late_streak >= 3:
                    return False
            else:
                late_streak = 0

        return True


class SolutionRegex:
    """Using regex"""

    def checkRecord(self, s: str) -> bool:
        import re
        # Match if: has 2+ A's OR has 3+ consecutive L's
        return not re.search(r'A.*A|LLL', s)
