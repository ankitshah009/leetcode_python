#1704. Determine if String Halves Are Alike
#Easy
#
#You are given a string s of even length. Split this string into two halves of
#equal lengths, and let a be the first half and b be the second half.
#
#Two strings are alike if they have the same number of vowels ('a', 'e', 'i',
#'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and
#lowercase letters.
#
#Return true if a and b are alike. Otherwise, return false.
#
#Example 1:
#Input: s = "book"
#Output: true
#
#Example 2:
#Input: s = "textbook"
#Output: false
#
#Constraints:
#    2 <= s.length <= 1000
#    s.length is even.
#    s consists of uppercase and lowercase letters.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Count vowels in each half.
        """
        vowels = set('aeiouAEIOU')
        n = len(s)
        mid = n // 2

        count1 = sum(1 for c in s[:mid] if c in vowels)
        count2 = sum(1 for c in s[mid:] if c in vowels)

        return count1 == count2


class SolutionOnePass:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Single pass with balance counter.
        """
        vowels = set('aeiouAEIOU')
        n = len(s)
        mid = n // 2
        balance = 0

        for i in range(n):
            if s[i] in vowels:
                balance += 1 if i < mid else -1

        return balance == 0


class SolutionCounter:
    def halvesAreAlike(self, s: str) -> bool:
        """
        Using Counter.
        """
        from collections import Counter

        vowels = set('aeiouAEIOU')
        mid = len(s) // 2

        c1 = Counter(c for c in s[:mid] if c in vowels)
        c2 = Counter(c for c in s[mid:] if c in vowels)

        return sum(c1.values()) == sum(c2.values())
