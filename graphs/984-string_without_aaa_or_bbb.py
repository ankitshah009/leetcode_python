#984. String Without AAA or BBB
#Medium
#
#Given two integers a and b, return any string s such that:
#- s has length a + b and contains exactly a 'a' letters and exactly b 'b' letters,
#- The substring 'aaa' does not occur in s, and
#- The substring 'bbb' does not occur in s.
#
#Example 1:
#Input: a = 1, b = 2
#Output: "abb"
#
#Example 2:
#Input: a = 4, b = 1
#Output: "aabaa"
#
#Constraints:
#    0 <= a, b <= 100
#    It is guaranteed such an s exists for the given a and b.

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        """
        Greedy: add 2 of majority, 1 of minority.
        """
        result = []

        while a > 0 or b > 0:
            # Check last 2 chars
            if len(result) >= 2 and result[-1] == result[-2]:
                # Must switch
                if result[-1] == 'a':
                    result.append('b')
                    b -= 1
                else:
                    result.append('a')
                    a -= 1
            else:
                # Add majority
                if a >= b:
                    result.append('a')
                    a -= 1
                else:
                    result.append('b')
                    b -= 1

        return ''.join(result)


class SolutionPattern:
    """Build with pattern"""

    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []

        while a > 0 and b > 0:
            if a > b:
                result.append('aa')
                a -= 2
                result.append('b')
                b -= 1
            elif b > a:
                result.append('bb')
                b -= 2
                result.append('a')
                a -= 1
            else:
                result.append('ab')
                a -= 1
                b -= 1

        # Remaining
        if a > 0:
            result.append('a' * a)
        if b > 0:
            result.append('b' * b)

        return ''.join(result)


class SolutionExplicit:
    """More explicit greedy"""

    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []

        while a > 0 or b > 0:
            add_a = False

            if len(result) >= 2 and result[-1] == 'a' and result[-2] == 'a':
                add_a = False
            elif len(result) >= 2 and result[-1] == 'b' and result[-2] == 'b':
                add_a = True
            elif a >= b:
                add_a = True
            else:
                add_a = False

            if add_a:
                result.append('a')
                a -= 1
            else:
                result.append('b')
                b -= 1

        return ''.join(result)
