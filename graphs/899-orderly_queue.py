#899. Orderly Queue
#Hard
#
#You are given a string s and an integer k. You can choose one of the first k
#letters of s and append it at the end of the string.
#
#Return the lexicographically smallest string you could have after applying the
#mentioned step any number of moves.
#
#Example 1:
#Input: s = "cba", k = 1
#Output: "acb"
#Explanation: We apply move 3 times: "cba" -> "bac" -> "acb".
#
#Example 2:
#Input: s = "baaca", k = 3
#Output: "aaabc"
#Explanation: We can always sort the string if k >= 2.
#
#Constraints:
#    1 <= k <= s.length <= 1000
#    s consist of lowercase English letters.

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        If k == 1: can only rotate, return smallest rotation.
        If k >= 2: can achieve any permutation, return sorted string.
        """
        if k == 1:
            # Find lexicographically smallest rotation
            rotations = [s[i:] + s[:i] for i in range(len(s))]
            return min(rotations)
        else:
            # Can sort to any permutation
            return ''.join(sorted(s))


class SolutionExplained:
    """With proof explanation"""

    def orderlyQueue(self, s: str, k: int) -> str:
        """
        For k >= 2, we can perform bubble sort:
        - With k >= 2, we can swap any two adjacent characters
        - By moving first char, then second char, we effectively swap them

        For k == 1, we can only rotate the string.
        """
        if k >= 2:
            return ''.join(sorted(s))

        # k == 1: try all rotations
        min_str = s
        for i in range(1, len(s)):
            rotated = s[i:] + s[:i]
            if rotated < min_str:
                min_str = rotated

        return min_str


class SolutionOptimized:
    """Optimized rotation finding using Booth's algorithm concept"""

    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return ''.join(sorted(s))

        # Find minimum rotation using doubling trick
        doubled = s + s
        n = len(s)
        min_start = 0

        for i in range(1, n):
            if doubled[i:i+n] < doubled[min_start:min_start+n]:
                min_start = i

        return s[min_start:] + s[:min_start]
