#859. Buddy Strings
#Easy
#
#Given two strings s and goal, return true if you can swap two letters in s so
#the result is equal to goal, otherwise, return false.
#
#Swapping letters is defined as taking two indices i and j (0-indexed) such that
#i != j and swapping the characters at s[i] and s[j].
#
#Example 1:
#Input: s = "ab", goal = "ba"
#Output: true
#Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba".
#
#Example 2:
#Input: s = "ab", goal = "ab"
#Output: false
#Explanation: You can only swap s[0] = 'a' and s[1] = 'b', which results in "ba".
#
#Example 3:
#Input: s = "aa", goal = "aa"
#Output: true
#Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa".
#
#Constraints:
#    1 <= s.length, goal.length <= 2 * 10^4
#    s and goal consist of lowercase letters.

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        """
        Two cases:
        1. s == goal: need duplicate characters to swap
        2. s != goal: exactly 2 positions differ, and swapping fixes them
        """
        if len(s) != len(goal):
            return False

        if s == goal:
            # Need at least one duplicate character
            return len(set(s)) < len(s)

        # Find differences
        diff = [(a, b) for a, b in zip(s, goal) if a != b]

        # Exactly 2 differences, and swapping fixes them
        return len(diff) == 2 and diff[0] == diff[1][::-1]


class SolutionExplicit:
    """More explicit logic"""

    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        # Find positions where s and goal differ
        diff_positions = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_positions.append(i)

        # Case 1: No differences - need duplicate to make a valid swap
        if len(diff_positions) == 0:
            return len(s) != len(set(s))

        # Case 2: Exactly 2 differences
        if len(diff_positions) == 2:
            i, j = diff_positions
            return s[i] == goal[j] and s[j] == goal[i]

        # Other cases: impossible
        return False


class SolutionCounter:
    """Using Counter"""

    def buddyStrings(self, s: str, goal: str) -> bool:
        from collections import Counter

        if len(s) != len(goal):
            return False

        if Counter(s) != Counter(goal):
            return False

        diff = sum(1 for a, b in zip(s, goal) if a != b)

        if diff == 0:
            return len(s) != len(set(s))

        return diff == 2
