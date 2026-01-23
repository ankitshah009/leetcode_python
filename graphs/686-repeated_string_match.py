#686. Repeated String Match
#Medium
#
#Given two strings a and b, return the minimum number of times you should repeat
#string a so that string b is a substring of it. If it is impossible for b to
#be a substring of a after repeating it, return -1.
#
#Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and
#repeated 2 times is "abcabc".
#
#Example 1:
#Input: a = "abcd", b = "cdabcdab"
#Output: 3
#Explanation: We return 3 because by repeating a three times "abcdabcdabcd",
#b is a substring of it.
#
#Example 2:
#Input: a = "a", b = "aa"
#Output: 2
#
#Example 3:
#Input: a = "a", b = "a"
#Output: 1
#
#Example 4:
#Input: a = "abc", b = "wxyz"
#Output: -1
#
#Constraints:
#    1 <= a.length, b.length <= 10^4
#    a and b consist of lowercase English letters.

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """
        Repeat a until it's at least as long as b, then check substring.
        May need one extra repetition for boundary cases.
        """
        # Minimum repetitions needed
        times = (len(b) + len(a) - 1) // len(a)

        repeated = a * times
        if b in repeated:
            return times

        repeated += a
        if b in repeated:
            return times + 1

        return -1


class SolutionKMP:
    """Using KMP algorithm for substring search"""

    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Build failure function for b
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    i += 1
            return lps

        # Check if b contains only characters from a
        if not set(b).issubset(set(a)):
            return -1

        times = (len(b) + len(a) - 1) // len(a)

        # KMP search
        lps = build_lps(b)

        for extra in range(2):
            text = a * (times + extra)
            j = 0
            for i in range(len(text)):
                while j and text[i] != b[j]:
                    j = lps[j - 1]
                if text[i] == b[j]:
                    j += 1
                if j == len(b):
                    return times + extra

        return -1


class SolutionRabinKarp:
    """Using Rabin-Karp rolling hash"""

    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not set(b).issubset(set(a)):
            return -1

        times = (len(b) + len(a) - 1) // len(a)

        for extra in range(2):
            if b in a * (times + extra):
                return times + extra

        return -1
