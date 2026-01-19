#249. Group Shifted Strings
#Medium
#
#We can shift a string by shifting each of its letters to its successive letter.
#For example, "abc" can be shifted to be "bcd".
#
#We can keep shifting the string to form a sequence.
#For example, we can keep shifting "abc" to form the sequence:
#"abc" -> "bcd" -> ... -> "xyz".
#
#Given an array of strings strings, group all strings that belong to the same
#shifting sequence. You may return the answer in any order.
#
#Example 1:
#Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
#Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
#
#Example 2:
#Input: strings = ["a"]
#Output: [["a"]]
#
#Constraints:
#    1 <= strings.length <= 200
#    1 <= strings[i].length <= 50
#    strings[i] consists of lowercase English letters.

from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        Key insight: strings in same group have same "shift pattern".
        Pattern = differences between consecutive characters (mod 26).
        """
        groups = defaultdict(list)

        for s in strings:
            # Generate key based on differences
            key = self.get_key(s)
            groups[key].append(s)

        return list(groups.values())

    def get_key(self, s):
        if len(s) == 1:
            return ()

        diffs = []
        for i in range(1, len(s)):
            diff = (ord(s[i]) - ord(s[i-1])) % 26
            diffs.append(diff)

        return tuple(diffs)


class SolutionNormalize:
    """Normalize string to start with 'a'"""

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strings:
            # Shift string so first character is 'a'
            shift = ord(s[0]) - ord('a')
            normalized = ''.join(
                chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
                for c in s
            )
            groups[normalized].append(s)

        return list(groups.values())


class SolutionHash:
    """Using a hash of differences"""

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strings:
            # Create key from character differences
            if len(s) == 1:
                key = (0,)
            else:
                key = tuple(
                    (ord(s[i+1]) - ord(s[i])) % 26
                    for i in range(len(s) - 1)
                )

            groups[key].append(s)

        return list(groups.values())
