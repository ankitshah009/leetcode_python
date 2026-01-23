#1520. Maximum Number of Non-Overlapping Substrings
#Hard
#
#Given a string s of lowercase letters, you need to find the maximum number of
#non-empty substrings of s that meet the following conditions:
#
#    The substrings do not overlap, that is for any two substrings s[i..j] and
#    s[x..y], either j < x or i > y is true.
#    A substring that contains a certain character c must also contain all
#    occurrences of c.
#
#Find the maximum number of substrings that meet the above conditions. If there
#are multiple solutions with the same number of substrings, return the one with
#minimum total length. It can be shown that there exists a unique solution of
#minimum total length.
#
#Notice that you can return the substrings in any order.
#
#Example 1:
#Input: s = "adefaddaccc"
#Output: ["e","f","ccc"]
#Explanation: The following are all the possible substrings that meet the conditions:
#[  "adefaddaccc"  "adefadda",  "ef",  "e",  "f",  "ccc"]
#If we choose the first string, we cannot choose anything else and we'd get only 1.
#If we choose "adefadda", we are left with "ccc" which is the only one that
#doesn't overlap, thus obtaining 2 substrings.
#Notice also, that it's not optimal to choose "ef" since it can be split into two.
#Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings.
#No other solution of the same number of substrings exist.
#
#Example 2:
#Input: s = "abbaccd"
#Output: ["d","bb","cc"]
#Explanation: Notice that while the set of substrings ["d","abba","cc"] also has
#length 3, it's considered incorrect since it has larger total length.
#
#Constraints:
#    1 <= s.length <= 10^5
#    s contains only lowercase English letters.

from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        """
        1. Find first and last occurrence of each character.
        2. For each character, expand interval to include all chars that must be included.
        3. Greedily select non-overlapping intervals preferring shorter ones.
        """
        n = len(s)

        # Find first and last occurrence of each character
        first = {}
        last = {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        def get_interval(c: str) -> tuple:
            """
            Get the minimum interval that contains all occurrences of c
            and all occurrences of any other char within that interval.
            Returns (left, right) or (-1, -1) if invalid.
            """
            left = first[c]
            right = last[c]

            i = left
            while i <= right:
                char = s[i]
                if first[char] < left:
                    return (-1, -1)  # Cannot form valid interval starting at 'left'
                right = max(right, last[char])
                i += 1

            return (left, right)

        # Get all valid intervals
        intervals = []
        for c in first:
            interval = get_interval(c)
            if interval != (-1, -1):
                intervals.append(interval)

        # Sort by right endpoint (greedy interval scheduling)
        intervals.sort(key=lambda x: x[1])

        # Greedily select non-overlapping intervals
        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                # Check if this is the smallest interval ending at 'right'
                # (we already sorted by right, so first one encountered is smallest)
                result.append(s[left:right + 1])
                prev_end = right

        return result


class SolutionAlternative:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        """
        Alternative implementation with explicit interval expansion.
        """
        n = len(s)

        # First and last positions
        first = [n] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if first[idx] == n:
                first[idx] = i
            last[idx] = i

        def expand_interval(left: int) -> int:
            """
            Expand interval starting at 'left' to include all required chars.
            Returns the right endpoint, or -1 if interval must start earlier.
            """
            right = last[ord(s[left]) - ord('a')]
            i = left

            while i <= right:
                idx = ord(s[i]) - ord('a')
                if first[idx] < left:
                    return -1
                right = max(right, last[idx])
                i += 1

            return right

        # Find all valid intervals starting at each character's first occurrence
        intervals = []
        for c in range(26):
            if first[c] < n:
                right = expand_interval(first[c])
                if right != -1:
                    intervals.append((first[c], right))

        # Sort by right endpoint
        intervals.sort(key=lambda x: x[1])

        # Greedy selection
        result = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result
