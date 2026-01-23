#1153. String Transforms Into Another String
#Hard
#
#Given two strings str1 and str2 of the same length, determine whether you can
#transform str1 into str2 by doing zero or more conversions.
#
#In one conversion you can convert all occurrences of one character in str1 to
#any other character.
#
#Return true if and only if you can transform str1 into str2.
#
#Example 1:
#Input: str1 = "aabcc", str2 = "ccdee"
#Output: true
#Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'.
#Note that the order of conversions matter.
#
#Example 2:
#Input: str1 = "leetcode", str2 = "codeleet"
#Output: false
#Explanation: There is no way to transform str1 to str2.
#
#Constraints:
#    1 <= str1.length == str2.length <= 10^4
#    str1 and str2 contain only lowercase English letters.

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """
        Key insights:
        1. Each char in str1 can only map to one char in str2
        2. If str2 uses all 26 letters and str1 != str2, impossible
           (no temp char available for swaps)
        """
        if str1 == str2:
            return True

        # Build mapping from str1 chars to str2 chars
        mapping = {}

        for c1, c2 in zip(str1, str2):
            if c1 in mapping:
                if mapping[c1] != c2:
                    return False  # Conflicting mapping
            else:
                mapping[c1] = c2

        # If str2 uses all 26 letters, we can't do conversions
        # (need a temp character for intermediate steps)
        return len(set(str2)) < 26


class SolutionDetailed:
    def canConvert(self, str1: str, str2: str) -> bool:
        """More detailed explanation"""
        if str1 == str2:
            return True

        # Check 1: Each char in str1 maps to exactly one char in str2
        char_map = {}
        for i in range(len(str1)):
            c1, c2 = str1[i], str2[i]
            if c1 in char_map:
                if char_map[c1] != c2:
                    # Same char maps to different targets
                    return False
            else:
                char_map[c1] = c2

        # Check 2: Need at least one unused char in str2 for temp storage
        # This handles cycles like a->b->a
        # We need a temp char to break cycles
        unique_targets = set(str2)

        # If all 26 letters are used in str2, no temp char available
        return len(unique_targets) < 26
