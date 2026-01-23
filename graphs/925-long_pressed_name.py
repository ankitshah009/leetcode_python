#925. Long Pressed Name
#Easy
#
#Your friend is typing his name into a keyboard. Sometimes, when typing a
#character c, the key might get long pressed, and the character will be typed
#1 or more times.
#
#You examine the typed characters. Return True if it is possible that it was
#your friends name, with some characters (possibly none) being long pressed.
#
#Example 1:
#Input: name = "alex", typed = "aaleex"
#Output: true
#
#Example 2:
#Input: name = "saeed", typed = "ssaaedd"
#Output: false
#Explanation: 'e' must have been pressed twice, but it was not.
#
#Constraints:
#    1 <= name.length, typed.length <= 1000
#    name and typed consist of only lowercase English letters.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        Two pointers: typed must contain all chars of name in order,
        with possible repeats.
        """
        i = 0  # Pointer for name
        j = 0  # Pointer for typed

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False

        return i == len(name)


class SolutionGroupBy:
    """Group consecutive chars"""

    def isLongPressedName(self, name: str, typed: str) -> bool:
        def group(s):
            groups = []
            i = 0
            while i < len(s):
                char = s[i]
                count = 0
                while i < len(s) and s[i] == char:
                    count += 1
                    i += 1
                groups.append((char, count))
            return groups

        name_groups = group(name)
        typed_groups = group(typed)

        if len(name_groups) != len(typed_groups):
            return False

        for (c1, n1), (c2, n2) in zip(name_groups, typed_groups):
            if c1 != c2 or n1 > n2:
                return False

        return True


class SolutionItertools:
    """Using itertools.groupby"""

    def isLongPressedName(self, name: str, typed: str) -> bool:
        from itertools import groupby

        def encode(s):
            return [(char, len(list(group))) for char, group in groupby(s)]

        name_enc = encode(name)
        typed_enc = encode(typed)

        if len(name_enc) != len(typed_enc):
            return False

        return all(c1 == c2 and n1 <= n2
                   for (c1, n1), (c2, n2) in zip(name_enc, typed_enc))
