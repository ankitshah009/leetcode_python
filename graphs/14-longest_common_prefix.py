#14. Longest Common Prefix
#Easy
#
#Write a function to find the longest common prefix string amongst an array of
#strings.
#
#If there is no common prefix, return an empty string "".
#
#Example 1:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#
#Example 2:
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
#
#Constraints:
#    1 <= strs.length <= 200
#    0 <= strs[i].length <= 200
#    strs[i] consists of only lowercase English letters.

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Vertical scanning - compare characters column by column.
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]

        return strs[0]


class SolutionHorizontal:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Horizontal scanning - find LCP between first two, then with third, etc.
        """
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


class SolutionDivideConquer:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Divide and conquer approach.
        """
        def common_prefix(left: str, right: str) -> str:
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]

        def lcp(strs: List[str], l: int, r: int) -> str:
            if l == r:
                return strs[l]

            mid = (l + r) // 2
            lcp_left = lcp(strs, l, mid)
            lcp_right = lcp(strs, mid + 1, r)

            return common_prefix(lcp_left, lcp_right)

        if not strs:
            return ""

        return lcp(strs, 0, len(strs) - 1)


class SolutionBinarySearch:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Binary search on prefix length.
        """
        def is_common_prefix(length: int) -> bool:
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)

        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        left, right = 0, min_len

        while left < right:
            mid = (left + right + 1) // 2
            if is_common_prefix(mid):
                left = mid
            else:
                right = mid - 1

        return strs[0][:left]


class SolutionSorting:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Sort and compare only first and last strings.
        """
        if not strs:
            return ""

        strs.sort()

        first, last = strs[0], strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]


class SolutionZip:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Pythonic solution using zip.
        """
        if not strs:
            return ""

        prefix = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix.append(chars[0])
            else:
                break

        return ''.join(prefix)
