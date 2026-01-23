#1525. Number of Good Ways to Split a String
#Medium
#
#You are given a string s.
#
#A split is called good if you can split s into two non-empty strings sleft and
#sright where their concatenation is equal to s (i.e., sleft + sright = s) and
#the number of distinct letters in sleft and sright is the same.
#
#Return the number of good splits you can make in s.
#
#Example 1:
#Input: s = "aacaba"
#Output: 2
#Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
#("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
#("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
#("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
#("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
#("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
#
#Example 2:
#Input: s = "abcd"
#Output: 1
#Explanation: Split the string as follows ("ab", "cd").
#
#Constraints:
#    1 <= s.length <= 10^5
#    s consists of only lowercase English letters.

from collections import Counter

class Solution:
    def numSplits(self, s: str) -> int:
        """
        Precompute distinct chars from left and right for each split point.
        """
        n = len(s)

        # left_distinct[i] = distinct chars in s[0:i+1]
        left_distinct = [0] * n
        seen = set()
        for i in range(n):
            seen.add(s[i])
            left_distinct[i] = len(seen)

        # right_distinct[i] = distinct chars in s[i:n]
        right_distinct = [0] * n
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            right_distinct[i] = len(seen)

        # Count good splits: split after index i means left = s[0:i+1], right = s[i+1:n]
        count = 0
        for i in range(n - 1):
            if left_distinct[i] == right_distinct[i + 1]:
                count += 1

        return count


class SolutionOnePass:
    def numSplits(self, s: str) -> int:
        """
        Two-pointer approach with running counts.
        """
        n = len(s)

        # Count all chars on the right initially
        right_count = Counter(s)
        right_distinct = len(right_count)

        left_count = Counter()
        left_distinct = 0

        count = 0

        for i in range(n - 1):
            char = s[i]

            # Move char from right to left
            if left_count[char] == 0:
                left_distinct += 1
            left_count[char] += 1

            right_count[char] -= 1
            if right_count[char] == 0:
                right_distinct -= 1

            if left_distinct == right_distinct:
                count += 1

        return count


class SolutionArray:
    def numSplits(self, s: str) -> int:
        """
        Using arrays instead of Counter for efficiency.
        """
        n = len(s)

        # Right counts
        right = [0] * 26
        for c in s:
            right[ord(c) - ord('a')] += 1

        right_distinct = sum(1 for x in right if x > 0)

        left = [0] * 26
        left_distinct = 0
        count = 0

        for i in range(n - 1):
            idx = ord(s[i]) - ord('a')

            # Add to left
            if left[idx] == 0:
                left_distinct += 1
            left[idx] += 1

            # Remove from right
            right[idx] -= 1
            if right[idx] == 0:
                right_distinct -= 1

            if left_distinct == right_distinct:
                count += 1

        return count


class SolutionSet:
    def numSplits(self, s: str) -> int:
        """
        Using set for tracking distinct characters.
        """
        n = len(s)

        # Build prefix distinct counts
        prefix_distinct = []
        seen = set()
        for c in s:
            seen.add(c)
            prefix_distinct.append(len(seen))

        # Build suffix distinct counts
        suffix_distinct = [0] * n
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            suffix_distinct[i] = len(seen)

        # Count matches
        return sum(1 for i in range(n - 1) if prefix_distinct[i] == suffix_distinct[i + 1])
