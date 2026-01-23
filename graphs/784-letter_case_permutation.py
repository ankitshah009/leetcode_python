#784. Letter Case Permutation
#Medium
#
#Given a string s, you can transform every letter individually to be lowercase
#or uppercase to create another string.
#
#Return a list of all possible strings we could create. Return the output in
#any order.
#
#Example 1:
#Input: s = "a1b2"
#Output: ["a1b2","a1B2","A1b2","A1B2"]
#
#Example 2:
#Input: s = "3z4"
#Output: ["3z4","3Z4"]
#
#Constraints:
#    1 <= s.length <= 12
#    s consists of lowercase English letters, uppercase English letters, and digits.

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        """
        Backtracking: for each letter, try both cases.
        """
        result = []

        def backtrack(i, current):
            if i == len(s):
                result.append(''.join(current))
                return

            if s[i].isalpha():
                # Try lowercase
                current.append(s[i].lower())
                backtrack(i + 1, current)
                current.pop()

                # Try uppercase
                current.append(s[i].upper())
                backtrack(i + 1, current)
                current.pop()
            else:
                current.append(s[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result


class SolutionIterative:
    """Build permutations iteratively"""

    def letterCasePermutation(self, s: str) -> list[str]:
        result = ['']

        for c in s:
            if c.isalpha():
                result = [r + case for r in result for case in (c.lower(), c.upper())]
            else:
                result = [r + c for r in result]

        return result


class SolutionBitmask:
    """Use bitmask for letter positions"""

    def letterCasePermutation(self, s: str) -> list[str]:
        letters = [i for i, c in enumerate(s) if c.isalpha()]
        n = len(letters)

        result = []

        for mask in range(1 << n):
            chars = list(s.lower())
            for i, idx in enumerate(letters):
                if mask & (1 << i):
                    chars[idx] = chars[idx].upper()
            result.append(''.join(chars))

        return result


class SolutionProduct:
    """Using itertools.product"""

    def letterCasePermutation(self, s: str) -> list[str]:
        from itertools import product

        choices = []
        for c in s:
            if c.isalpha():
                choices.append([c.lower(), c.upper()])
            else:
                choices.append([c])

        return [''.join(p) for p in product(*choices)]
