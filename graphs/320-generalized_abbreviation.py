#320. Generalized Abbreviation
#Medium
#
#A word's generalized abbreviation can be constructed by taking any number of
#non-overlapping and non-adjacent substrings and replacing them with their
#respective lengths.
#
#For example, "abcde" can be abbreviated into:
#"a]bcde" ("a" + "bcde")
#"a3e" ("a" + "bcd" + "e")
#"5" ("abcde")
#etc.
#
#Given a string word, return a list of all the possible generalized
#abbreviations of word. Return the answer in any order.
#
#Example 1:
#Input: word = "word"
#Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1",
#         "w1rd","wo2","wo1d","wor1","word"]
#
#Example 2:
#Input: word = "a"
#Output: ["1","a"]
#
#Constraints:
#    1 <= word.length <= 15
#    word consists of only lowercase English letters.

from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        """Backtracking approach"""
        result = []
        n = len(word)

        def backtrack(pos, current, count):
            if pos == n:
                # Add remaining count if any
                if count > 0:
                    current += str(count)
                result.append(current)
                return

            # Option 1: Abbreviate current character (increment count)
            backtrack(pos + 1, current, count + 1)

            # Option 2: Keep current character
            if count > 0:
                current += str(count)
            backtrack(pos + 1, current + word[pos], 0)

        backtrack(0, "", 0)
        return result


class SolutionBitmask:
    """Using bitmask to generate all combinations"""

    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        result = []

        # Each bit represents whether to keep (1) or abbreviate (0)
        for mask in range(1 << n):
            abbr = []
            count = 0

            for i in range(n):
                if mask & (1 << i):
                    # Keep this character
                    if count > 0:
                        abbr.append(str(count))
                        count = 0
                    abbr.append(word[i])
                else:
                    # Abbreviate
                    count += 1

            if count > 0:
                abbr.append(str(count))

            result.append(''.join(abbr))

        return result


class SolutionIterative:
    """Iterative approach"""

    def generateAbbreviations(self, word: str) -> List[str]:
        result = [""]

        for c in word:
            new_result = []
            for abbr in result:
                # Option 1: Abbreviate (add 1 or increment last number)
                if abbr and abbr[-1].isdigit():
                    # Find and increment the number
                    i = len(abbr) - 1
                    while i >= 0 and abbr[i].isdigit():
                        i -= 1
                    num = int(abbr[i+1:]) + 1
                    new_result.append(abbr[:i+1] + str(num))
                else:
                    new_result.append(abbr + "1")

                # Option 2: Keep character
                new_result.append(abbr + c)

            result = new_result

        return result
