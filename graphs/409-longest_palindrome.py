#409. Longest Palindrome
#Easy
#
#Given a string s which consists of lowercase or uppercase letters, return the
#length of the longest palindrome that can be built with those letters.
#
#Letters are case sensitive, for example, "Aa" is not considered a palindrome.
#
#Example 1:
#Input: s = "abccccdd"
#Output: 7
#Explanation: One longest palindrome that can be built is "dccaccd", whose
#length is 7.
#
#Example 2:
#Input: s = "a"
#Output: 1
#Explanation: The longest palindrome that can be built is "a", whose length is
#1.
#
#Constraints:
#    1 <= s.length <= 2000
#    s consists of lowercase and/or uppercase English letters only.

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Count characters. Use all pairs. Add 1 for center if any odd count.
        """
        count = Counter(s)
        length = 0
        has_odd = False

        for cnt in count.values():
            length += cnt // 2 * 2  # Use pairs
            if cnt % 2 == 1:
                has_odd = True

        return length + (1 if has_odd else 0)


class SolutionSet:
    """Using set to track odd counts"""

    def longestPalindrome(self, s: str) -> int:
        odds = set()

        for c in s:
            if c in odds:
                odds.remove(c)
            else:
                odds.add(c)

        # Total pairs + 1 center (if any odds)
        pairs = len(s) - len(odds)
        return pairs + (1 if odds else 0)


class SolutionOddCount:
    """Count odd occurrences"""

    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        odd_count = sum(1 for cnt in count.values() if cnt % 2 == 1)

        # Use all characters except (odd_count - 1) to make pairs
        # Keep 1 odd for center
        return len(s) - odd_count + (1 if odd_count > 0 else 0)


class SolutionArray:
    """Using array for character counts"""

    def longestPalindrome(self, s: str) -> int:
        count = [0] * 128  # ASCII

        for c in s:
            count[ord(c)] += 1

        length = 0
        has_odd = False

        for cnt in count:
            length += cnt // 2 * 2
            if cnt % 2 == 1:
                has_odd = True

        return length + (1 if has_odd else 0)
