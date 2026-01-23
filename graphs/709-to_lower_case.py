#709. To Lower Case
#Easy
#
#Given a string s, return the string after replacing every uppercase letter
#with the same lowercase letter.
#
#Example 1:
#Input: s = "Hello"
#Output: "hello"
#
#Example 2:
#Input: s = "here"
#Output: "here"
#
#Example 3:
#Input: s = "LOVELY"
#Output: "lovely"
#
#Constraints:
#    1 <= s.length <= 100
#    s consists of printable ASCII characters.

class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Use built-in lower() method.
        """
        return s.lower()


class SolutionASCII:
    """Manual conversion using ASCII values"""

    def toLowerCase(self, s: str) -> str:
        result = []
        for c in s:
            if 'A' <= c <= 'Z':
                # Add 32 to convert uppercase to lowercase
                result.append(chr(ord(c) + 32))
            else:
                result.append(c)
        return ''.join(result)


class SolutionBitManipulation:
    """Using bit manipulation: set 6th bit to make lowercase"""

    def toLowerCase(self, s: str) -> str:
        result = []
        for c in s:
            if 'A' <= c <= 'Z':
                # OR with 32 (0x20) sets the 6th bit
                result.append(chr(ord(c) | 32))
            else:
                result.append(c)
        return ''.join(result)


class SolutionComprehension:
    """One-liner using list comprehension"""

    def toLowerCase(self, s: str) -> str:
        return ''.join(
            chr(ord(c) + 32) if 'A' <= c <= 'Z' else c
            for c in s
        )


class SolutionMap:
    """Using map with lambda"""

    def toLowerCase(self, s: str) -> str:
        return ''.join(map(
            lambda c: chr(ord(c) + 32) if 'A' <= c <= 'Z' else c,
            s
        ))
