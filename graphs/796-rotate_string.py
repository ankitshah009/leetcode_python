#796. Rotate String
#Easy
#
#Given two strings s and goal, return true if and only if s can become goal
#after some number of shifts on s.
#
#A shift on s consists of moving the leftmost character of s to the rightmost
#position.
#
#Example 1:
#Input: s = "abcde", goal = "cdeab"
#Output: true
#
#Example 2:
#Input: s = "abcde", goal = "abced"
#Output: false
#
#Constraints:
#    1 <= s.length, goal.length <= 100
#    s and goal consist of lowercase English letters.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Key insight: goal is a rotation of s iff goal is a substring of s+s.
        """
        return len(s) == len(goal) and goal in s + s


class SolutionBruteForce:
    """Try all rotations"""

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False


class SolutionKMP:
    """Using KMP algorithm for substring search"""

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if not s:
            return True

        # Build failure function for goal
        n = len(goal)
        fail = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and goal[i] != goal[j]:
                j = fail[j - 1]
            if goal[i] == goal[j]:
                j += 1
            fail[i] = j

        # Search in s + s
        doubled = s + s
        j = 0
        for i in range(len(doubled)):
            while j > 0 and doubled[i] != goal[j]:
                j = fail[j - 1]
            if doubled[i] == goal[j]:
                j += 1
            if j == n:
                return True

        return False


class SolutionDeque:
    """Using deque for rotation"""

    def rotateString(self, s: str, goal: str) -> bool:
        from collections import deque

        if len(s) != len(goal):
            return False

        d = deque(s)
        for _ in range(len(s)):
            if ''.join(d) == goal:
                return True
            d.append(d.popleft())

        return False
