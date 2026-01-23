#1324. Print Words Vertically
#Medium
#
#Given a string s. Return all the words vertically in the same order in which
#they appear in s.
#Words are returned as a list of strings, complete with spaces when is necessary.
#(Trailing spaces are not allowed).
#Each word would be put on only one column and that in one column there will be
#only one word.
#
#Example 1:
#Input: s = "HOW ARE YOU"
#Output: ["HAY","ORE","WOU"]
#Explanation: Each word is printed vertically.
# "HAY"
# "ORE"
# "WOU"
#
#Example 2:
#Input: s = "TO BE OR NOT TO BE"
#Output: ["TBONTB","OEROOE","   T"]
#Explanation: Trailing spaces is not allowed.
# "TBONTB"
# "OEROOE"
# "   T"
#
#Example 3:
#Input: s = "CONTEST IS COMING"
#Output: ["CIC","OSO","N M","T I","E N","S G","T"]
#
#Constraints:
#    1 <= s.length <= 200
#    s contains only upper case English letters.
#    It's guaranteed that there is only one space between 2 words.

from typing import List
from itertools import zip_longest

class Solution:
    def printVertically(self, s: str) -> List[str]:
        """
        Split into words, then transpose.
        """
        words = s.split()
        max_len = max(len(w) for w in words)

        result = []
        for i in range(max_len):
            row = []
            for word in words:
                if i < len(word):
                    row.append(word[i])
                else:
                    row.append(' ')
            # Remove trailing spaces
            result.append(''.join(row).rstrip())

        return result


class SolutionZip:
    def printVertically(self, s: str) -> List[str]:
        """Using zip_longest for transposition"""
        words = s.split()
        # Transpose with space as fill value
        transposed = zip_longest(*words, fillvalue=' ')
        # Join and strip trailing spaces
        return [''.join(chars).rstrip() for chars in transposed]


class SolutionPadded:
    def printVertically(self, s: str) -> List[str]:
        """Pad all words to same length first"""
        words = s.split()
        max_len = max(len(w) for w in words)

        # Pad words
        padded = [w.ljust(max_len) for w in words]

        # Transpose
        result = []
        for i in range(max_len):
            col = ''.join(word[i] for word in padded)
            result.append(col.rstrip())

        return result
