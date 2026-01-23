#1585. Check If String Is Transformable With Substring Sort Operations
#Hard
#
#Given two strings s and t, transform string s into string t using the following
#operation any number of times:
#- Choose a non-empty substring in s and sort it in place so the characters are
#  in ascending order.
#
#For example, applying the operation on the underlined substring in "14234" results
#in "12344".
#
#Return true if it is possible to transform s into t. Otherwise, return false.
#
#A substring is a contiguous sequence of characters within a string.
#
#Example 1:
#Input: s = "84532", t = "34852"
#Output: true
#Explanation: You can transform s into t using the following sort operations:
#"84532" (from index 2 to 3) -> "84352"
#"84352" (from index 0 to 2) -> "34852"
#
#Example 2:
#Input: s = "34521", t = "23415"
#Output: true
#
#Example 3:
#Input: s = "12345", t = "12435"
#Output: false
#
#Constraints:
#    s.length == t.length
#    1 <= s.length <= 10^5
#    s and t consist of only digits.

from typing import List
from collections import deque

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        """
        Key insight: We can only move a smaller digit past larger digits
        to the left (via bubble sort). We cannot move a larger digit past
        smaller digits to the left.

        For each position in t, find the corresponding digit in s and check
        if all digits before it in s are larger (can be bubbled past).
        """
        # Store indices of each digit in s
        pos = [deque() for _ in range(10)]
        for i, c in enumerate(s):
            pos[int(c)].append(i)

        for c in t:
            d = int(c)

            # Check if digit d exists
            if not pos[d]:
                return False

            # Get the leftmost position of digit d
            idx = pos[d][0]

            # Check if any smaller digit is before idx
            # If so, we cannot move d to the front
            for smaller in range(d):
                if pos[smaller] and pos[smaller][0] < idx:
                    return False

            # Use this digit
            pos[d].popleft()

        return True


class SolutionDetailed:
    def isTransformable(self, s: str, t: str) -> bool:
        """
        Detailed solution with explanation.

        The operation is equivalent to bubble sort on substrings.
        In bubble sort, smaller elements can move left past larger ones,
        but larger elements cannot move left past smaller ones.

        For each target character, we need to check:
        1. The character exists in remaining s
        2. All characters before it (that haven't been matched) are >= it
        """
        # Track positions of each digit (0-9) in s
        indices = [[] for _ in range(10)]
        for i, ch in enumerate(s):
            indices[int(ch)].append(i)

        # Reverse to use as stack (pop from end = get leftmost)
        for i in range(10):
            indices[i] = indices[i][::-1]

        for ch in t:
            d = int(ch)

            # No more of this digit available
            if not indices[d]:
                return False

            # Current position of the digit we want to move
            curr_pos = indices[d][-1]

            # Check: no smaller digit should be at a position before curr_pos
            for smaller in range(d):
                if indices[smaller] and indices[smaller][-1] < curr_pos:
                    # There's a smaller digit that would block movement
                    return False

            # Use this digit (remove from available positions)
            indices[d].pop()

        return True


class SolutionInversionCount:
    def isTransformable(self, s: str, t: str) -> bool:
        """
        Alternative approach using position tracking.

        Track which positions of each digit in s we've used,
        and ensure ordering constraints are satisfied.
        """
        from collections import defaultdict

        # Build mapping: digit -> list of positions in s
        digit_positions = defaultdict(deque)
        for i, c in enumerate(s):
            digit_positions[c].append(i)

        # Check if t can be achieved
        for c in t:
            if not digit_positions[c]:
                return False

            pos = digit_positions[c][0]

            # Check all smaller digits
            for smaller_digit in range(int(c)):
                smaller_char = str(smaller_digit)
                if digit_positions[smaller_char]:
                    # If a smaller digit appears before our target
                    if digit_positions[smaller_char][0] < pos:
                        return False

            digit_positions[c].popleft()

        return True
