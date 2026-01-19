#763. Partition Labels
#Medium
#
#You are given a string s. We want to partition the string into as many parts as
#possible so that each letter appears in at most one part.
#
#Note that the partition is done so that after concatenating all the parts in
#order, the resultant string should be s.
#
#Return a list of integers representing the size of these parts.
#
#Example 1:
#Input: s = "ababcbacadefegdehijhklij"
#Output: [9,7,8]
#Explanation:
#The partition is "ababcbaca", "defegde", "hijhklij".
#This is a partition so that each letter appears in at most one part.
#
#Example 2:
#Input: s = "eccbbbbdec"
#Output: [10]
#
#Constraints:
#    1 <= s.length <= 500
#    s consists of lowercase English letters.

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        Greedy approach.
        For each character, find its last occurrence.
        Extend partition to include all last occurrences.
        """
        last = {c: i for i, c in enumerate(s)}

        result = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, last[c])

            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result


class SolutionMergeIntervals:
    """Convert to interval merging problem"""

    def partitionLabels(self, s: str) -> List[int]:
        # Find first and last occurrence of each character
        first = {}
        last = {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        # Create intervals
        intervals = [(first[c], last[c]) for c in first]
        intervals.sort()

        # Merge overlapping intervals
        result = []
        curr_start, curr_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= curr_end:
                curr_end = max(curr_end, end)
            else:
                result.append(curr_end - curr_start + 1)
                curr_start, curr_end = start, end

        result.append(curr_end - curr_start + 1)
        return result


class SolutionTwoPointers:
    """Two pointers with character tracking"""

    def partitionLabels(self, s: str) -> List[int]:
        result = []
        n = len(s)
        i = 0

        while i < n:
            # Find all characters that must be in this partition
            chars = set()
            j = i

            while j < n:
                if s[j] in chars or j == i:
                    chars.add(s[j])
                    # Extend j to last occurrence of s[j]
                    for k in range(n - 1, j, -1):
                        if s[k] == s[j]:
                            j = k
                            break
                j += 1
                if j > n - 1 or s[j] not in chars:
                    break

            result.append(j - i)
            i = j

        return result
