#791. Custom Sort String
#Medium
#
#You are given two strings order and s. All the characters of order are unique
#and were sorted in some custom order previously.
#
#Permute the characters of s so that they match the order that order was sorted.
#More specifically, if a character x occurs before a character y in order, then
#x should occur before y in the permuted string.
#
#Return any permutation of s that satisfies this property.
#
#Example 1:
#Input: order = "cba", s = "abcd"
#Output: "cbad"
#Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c"
#should be "c", "b", "a". Since "d" does not appear in order, it can be at
#any position in the returned string.
#
#Example 2:
#Input: order = "bcafg", s = "abcd"
#Output: "bcad"
#
#Constraints:
#    1 <= order.length <= 26
#    1 <= s.length <= 200
#    order and s consist of lowercase English letters.
#    All the characters of order are unique.

from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Count characters and build result following order.
        """
        count = Counter(s)
        result = []

        # Add characters in order
        for c in order:
            if c in count:
                result.append(c * count[c])
                del count[c]

        # Add remaining characters
        for c, cnt in count.items():
            result.append(c * cnt)

        return ''.join(result)


class SolutionCustomKey:
    """Using custom sort key"""

    def customSortString(self, order: str, s: str) -> str:
        order_map = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: order_map.get(x, 26)))


class SolutionBucket:
    """Bucket sort approach"""

    def customSortString(self, order: str, s: str) -> str:
        # 27 buckets: 0-25 for order chars, 26 for others
        buckets = [[] for _ in range(27)]
        order_idx = {c: i for i, c in enumerate(order)}

        for c in s:
            idx = order_idx.get(c, 26)
            buckets[idx].append(c)

        result = []
        for bucket in buckets:
            result.extend(bucket)

        return ''.join(result)
