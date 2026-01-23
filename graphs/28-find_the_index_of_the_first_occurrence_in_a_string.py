#28. Find the Index of the First Occurrence in a String
#Easy
#
#Given two strings needle and haystack, return the index of the first occurrence
#of needle in haystack, or -1 if needle is not part of haystack.
#
#Example 1:
#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.
#
#Example 2:
#Input: haystack = "leetcode", needle = "leeto"
#Output: -1
#Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#Constraints:
#    1 <= haystack.length, needle.length <= 10^4
#    haystack and needle consist of only lowercase English characters.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Sliding window approach - O(n*m).
        """
        if not needle:
            return 0

        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1


class SolutionKMP:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        KMP (Knuth-Morris-Pratt) algorithm - O(n+m).
        """
        if not needle:
            return 0

        # Build failure function
        m = len(needle)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # Search
        n = len(haystack)
        i = j = 0

        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1

                if j == m:
                    return i - j
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1


class SolutionRabinKarp:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Rabin-Karp algorithm with rolling hash - O(n+m) average.
        """
        if not needle:
            return 0

        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        # Hash parameters
        base = 26
        mod = 2**31 - 1

        # Calculate needle hash and first window hash
        needle_hash = 0
        window_hash = 0
        power = 1

        for i in range(m):
            needle_hash = (needle_hash * base + ord(needle[i])) % mod
            window_hash = (window_hash * base + ord(haystack[i])) % mod
            if i < m - 1:
                power = (power * base) % mod

        # Slide window
        for i in range(n - m + 1):
            if window_hash == needle_hash:
                # Verify to handle hash collision
                if haystack[i:i + m] == needle:
                    return i

            # Calculate next window hash
            if i < n - m:
                window_hash = ((window_hash - ord(haystack[i]) * power) * base +
                               ord(haystack[i + m])) % mod

        return -1


class SolutionBuiltin:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Using Python's built-in find method.
        """
        return haystack.find(needle)
