#1737. Change Minimum Characters to Satisfy One of Three Conditions
#Medium
#
#You are given two strings a and b that consist of lowercase letters. In one
#operation, you can change any character in a or b to any lowercase letter.
#
#Your goal is to satisfy one of the following three conditions:
#- Every letter in a is strictly less than every letter in b in the alphabet.
#- Every letter in b is strictly less than every letter in a in the alphabet.
#- Both a and b consist of only one distinct letter.
#
#Return the minimum number of operations needed to achieve your goal.
#
#Example 1:
#Input: a = "aba", b = "caa"
#Output: 2
#
#Example 2:
#Input: a = "dabadd", b = "cda"
#Output: 3
#
#Constraints:
#    1 <= a.length, b.length <= 10^5
#    a and b consist only of lowercase letters.

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        """
        Try all three conditions and return minimum.
        """
        from collections import Counter

        count_a = Counter(a)
        count_b = Counter(b)
        m, n = len(a), len(b)

        result = m + n  # Maximum possible

        # Condition 3: Make both strings consist of single letter
        for c in 'abcdefghijklmnopqrstuvwxyz':
            # Changes needed = total length - count of c in both
            cost = (m - count_a[c]) + (n - count_b[c])
            result = min(result, cost)

        # Conditions 1 and 2: One string all less than other
        # Try each letter as the boundary (a < boundary <= b or b < boundary <= a)

        # Prefix sums for characters <= threshold
        prefix_a = [0] * 27
        prefix_b = [0] * 27
        for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
            prefix_a[i + 1] = prefix_a[i] + count_a[c]
            prefix_b[i + 1] = prefix_b[i] + count_b[c]

        # Try boundary at each letter (1 to 25, not 0 or 26)
        for i in range(1, 26):
            # Condition 1: all of a < boundary, all of b >= boundary
            # Cost = chars in a >= boundary + chars in b < boundary
            cost1 = (m - prefix_a[i]) + prefix_b[i]
            result = min(result, cost1)

            # Condition 2: all of b < boundary, all of a >= boundary
            cost2 = (n - prefix_b[i]) + prefix_a[i]
            result = min(result, cost2)

        return result


class SolutionDetailed:
    def minCharacters(self, a: str, b: str) -> int:
        """
        Same approach with clearer variable names.
        """
        m, n = len(a), len(b)

        # Count frequencies
        freq_a = [0] * 26
        freq_b = [0] * 26
        for c in a:
            freq_a[ord(c) - ord('a')] += 1
        for c in b:
            freq_b[ord(c) - ord('a')] += 1

        result = m + n

        # Option 3: Make both strings single character
        for i in range(26):
            cost = (m - freq_a[i]) + (n - freq_b[i])
            result = min(result, cost)

        # Options 1 & 2: Boundary between characters
        sum_a = sum_b = 0
        for i in range(25):  # boundaries from 'a'/'b' to 'y'/'z'
            sum_a += freq_a[i]
            sum_b += freq_b[i]

            # Option 1: a all <= i, b all > i
            # Cost = chars in a > i + chars in b <= i
            cost1 = (m - sum_a) + sum_b
            result = min(result, cost1)

            # Option 2: b all <= i, a all > i
            cost2 = (n - sum_b) + sum_a
            result = min(result, cost2)

        return result
