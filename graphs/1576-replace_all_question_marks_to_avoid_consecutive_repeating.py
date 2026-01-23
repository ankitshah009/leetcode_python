#1576. Replace All ?'s to Avoid Consecutive Repeating Characters
#Easy
#
#Given a string s containing only lowercase English letters and the '?' character,
#convert all the '?' characters into lowercase letters such that the final string
#does not contain any consecutive repeating characters. You cannot modify the
#non '?' characters.
#
#It is guaranteed that there are no consecutive repeating characters in the given
#string except for '?'.
#
#Return the final string after all the conversions (possibly zero) have been made.
#If there is more than one solution, return any of them. It can be shown that an
#answer is always possible with the given constraints.
#
#Example 1:
#Input: s = "?zs"
#Output: "azs"
#Explanation: There are 25 solutions for this problem. "azs" is just one of them.
#
#Example 2:
#Input: s = "ubv?w"
#Output: "ubvaw"
#Explanation: There are 24 solutions for this problem. "ubvaw" is just one of them.
#
#Constraints:
#    1 <= s.length <= 100
#    s consist of lowercase English letters and '?'.

class Solution:
    def modifyString(self, s: str) -> str:
        """
        Replace each '?' with a letter different from neighbors.
        """
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == '?':
                # Find a letter different from left and right neighbors
                for c in 'abc':
                    left_ok = (i == 0 or s[i - 1] != c)
                    right_ok = (i == n - 1 or s[i + 1] != c)
                    if left_ok and right_ok:
                        s[i] = c
                        break

        return ''.join(s)


class SolutionSet:
    def modifyString(self, s: str) -> str:
        """
        Using set to find available letters.
        """
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == '?':
                forbidden = set()
                if i > 0:
                    forbidden.add(s[i - 1])
                if i < n - 1:
                    forbidden.add(s[i + 1])

                # Pick any letter not forbidden
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c not in forbidden:
                        s[i] = c
                        break

        return ''.join(s)


class SolutionOrd:
    def modifyString(self, s: str) -> str:
        """
        Using ord for letter iteration.
        """
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == '?':
                left = s[i - 1] if i > 0 else ''
                right = s[i + 1] if i < n - 1 else ''

                for code in range(ord('a'), ord('z') + 1):
                    c = chr(code)
                    if c != left and c != right:
                        s[i] = c
                        break

        return ''.join(s)


class SolutionSimple:
    def modifyString(self, s: str) -> str:
        """
        Simple approach: only need 3 letters.
        """
        result = list(s)

        for i in range(len(result)):
            if result[i] == '?':
                for c in 'abc':
                    if (i == 0 or result[i-1] != c) and (i == len(result)-1 or result[i+1] != c):
                        result[i] = c
                        break

        return ''.join(result)
