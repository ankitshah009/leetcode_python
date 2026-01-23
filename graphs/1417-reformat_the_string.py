#1417. Reformat The String
#Easy
#
#You are given an alphanumeric string s. (Alphanumeric string is a string
#consisting of lowercase English letters and digits).
#
#You have to find a permutation of the string where no letter is followed by
#another letter and no digit is followed by another digit. That is, no two
#adjacent characters have the same type.
#
#Return the reformatted string or return an empty string if it is impossible to
#reformat the string.
#
#Example 1:
#Input: s = "a0b1c2"
#Output: "0a1b2c"
#Explanation: No two adjacent characters have the same type in "0a1b2c".
#"a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
#
#Example 2:
#Input: s = "leetcode"
#Output: ""
#Explanation: "leetcode" has only characters so we cannot separate them by digits.
#
#Example 3:
#Input: s = "1229857369"
#Output: ""
#Explanation: "1229857369" has only digits so we cannot separate them by characters.
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of only lowercase English letters and/or digits.

class Solution:
    def reformat(self, s: str) -> str:
        """
        Separate letters and digits.
        Valid only if |len(letters) - len(digits)| <= 1.
        Interleave with longer group first.
        """
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        # Check if valid
        if abs(len(letters) - len(digits)) > 1:
            return ""

        # Put longer list first
        if len(letters) < len(digits):
            letters, digits = digits, letters

        # Interleave
        result = []
        for i in range(len(digits)):
            result.append(letters[i])
            result.append(digits[i])

        # If letters has one more
        if len(letters) > len(digits):
            result.append(letters[-1])

        return ''.join(result)


class SolutionAlternate:
    def reformat(self, s: str) -> str:
        """Using zip_longest for cleaner interleaving"""
        from itertools import zip_longest

        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        if len(letters) < len(digits):
            letters, digits = digits, letters

        result = []
        for a, b in zip_longest(letters, digits, fillvalue=''):
            result.append(a)
            result.append(b)

        return ''.join(result)


class SolutionInPlace:
    def reformat(self, s: str) -> str:
        """Build result character by character"""
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ""

        result = []
        # Determine which type goes at even indices
        if len(letters) >= len(digits):
            even_chars, odd_chars = letters, digits
        else:
            even_chars, odd_chars = digits, letters

        # Build string
        i, j = 0, 0
        for pos in range(len(s)):
            if pos % 2 == 0:
                result.append(even_chars[i])
                i += 1
            else:
                result.append(odd_chars[j])
                j += 1

        return ''.join(result)
