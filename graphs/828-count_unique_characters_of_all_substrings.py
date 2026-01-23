#828. Count Unique Characters of All Substrings of a Given String
#Hard
#
#Let's define a function countUniqueChars(s) that returns the number of unique
#characters of s.
#
#For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C",
#"O", "D" are the unique characters since they appear only once in s, therefore
#countUniqueChars(s) = 5.
#
#Given a string s, return the sum of countUniqueChars(t) where t is a substring
#of s. The test cases are generated such that the answer fits in a 32-bit integer.
#
#Notice that some substrings can be repeated so in this case you have to count
#the repeated ones too.
#
#Example 1:
#Input: s = "ABC"
#Output: 10
#Explanation: All possible substrings: "A","B","C","AB","BC","ABC"
#countUniqueChars("A") = 1, "B" = 1, "C" = 1, "AB" = 2, "BC" = 2, "ABC" = 3
#Total = 1 + 1 + 1 + 2 + 2 + 3 = 10
#
#Example 2:
#Input: s = "ABA"
#Output: 8
#Explanation: "ABA" contributes 1 unique char.
#
#Example 3:
#Input: s = "LEETCODE"
#Output: 92
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of uppercase English letters only.

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        For each character, count substrings where it's unique.
        Character at index i is unique in substring [left, right] if
        no other occurrence exists in that range.

        Contribution of char at i = (i - last_i) * (next_i - i)
        """
        from collections import defaultdict

        # Track indices of each character
        index = defaultdict(lambda: [-1])  # Previous occurrence

        for i, c in enumerate(s):
            index[c].append(i)

        for c in index:
            index[c].append(len(s))  # Next occurrence (sentinel)

        total = 0

        for c, positions in index.items():
            for i in range(1, len(positions) - 1):
                # positions[i] is the current occurrence
                # positions[i-1] is previous, positions[i+1] is next
                left = positions[i] - positions[i - 1]
                right = positions[i + 1] - positions[i]
                total += left * right

        return total


class SolutionSinglePass:
    """Single pass with last two occurrences"""

    def uniqueLetterString(self, s: str) -> int:
        # For each char, track last two positions
        last = {c: [-1, -1] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}

        total = 0

        for i, c in enumerate(s):
            # When we see char c at position i:
            # - Contribution starts from last[c][1] + 1 to i
            # - For the previous occurrence at last[c][1], update its contribution
            prev1, prev2 = last[c]
            # Character at prev2 contributes to substrings ending at positions
            # from prev2 to i-1, but we count as we go

            # Actually, use different formulation
            last[c] = [prev2, i]

        # Final pass
        last = {c: [-1, -1] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
        n = len(s)

        for i, c in enumerate(s):
            k, j = last[c]
            # Char at j contributes (j - k) for each ending position from j to i-1
            # That's (j - k) * (i - j) total
            total += (j - k) * (i - j)
            last[c] = [j, i]

        # Final contributions
        for c, (k, j) in last.items():
            total += (j - k) * (n - j)

        return total


class SolutionDP:
    """DP approach"""

    def uniqueLetterString(self, s: str) -> int:
        # contribution[i] = unique char contribution for substrings ending at i
        n = len(s)
        last_pos = {}  # Last position of each char
        second_last = {}  # Second to last position

        total = 0
        curr = 0  # Sum of unique chars for all substrings ending at current position

        for i, c in enumerate(s):
            # Update curr
            # New substrings ending at i: add contribution of c
            # c appears: remove old contribution, add new
            j = last_pos.get(c, -1)
            k = second_last.get(c, -1)

            # Remove old contribution of c at position j
            # Old: (j - k) for positions j to i-1
            curr -= (j - k)

            # Add new contribution of c at position i
            curr += (i - j)

            total += curr

            second_last[c] = j
            last_pos[c] = i

        return total
