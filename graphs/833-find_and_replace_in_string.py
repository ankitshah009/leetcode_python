#833. Find And Replace in String
#Medium
#
#You are given a 0-indexed string s that you must perform k replacement
#operations on. The replacement operations are given as three 0-indexed parallel
#arrays, indices, sources, and targets, all of length k.
#
#To complete the ith replacement operation:
#1. Check if the substring sources[i] occurs at index indices[i] in the
#   original string s.
#2. If it does not occur, do nothing.
#3. Otherwise if it does occur, replace that substring with targets[i].
#
#All replacement operations must occur simultaneously, meaning the replacement
#operations should not affect the indexing of each other. The testcases will be
#generated such that the replacements will not overlap.
#
#Example 1:
#Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
#Output: "eeebffff"
#
#Example 2:
#Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
#Output: "eeecd"
#
#Constraints:
#    1 <= s.length <= 1000
#    k == indices.length == sources.length == targets.length
#    1 <= k <= 100
#    0 <= indices[i] < s.length
#    1 <= sources[i].length, targets[i].length <= 50
#    s consists of only lowercase English letters.
#    sources[i] and targets[i] consist of only lowercase English letters.

class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        """
        Process replacements from right to left to maintain indices.
        """
        # Create list of (index, source, target) and sort by index descending
        replacements = sorted(zip(indices, sources, targets), reverse=True)

        s = list(s)

        for idx, source, target in replacements:
            # Check if source matches at idx
            if ''.join(s[idx:idx + len(source)]) == source:
                s[idx:idx + len(source)] = list(target)

        return ''.join(s)


class SolutionBuildResult:
    """Build result string directly"""

    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        # Map index to (source, target)
        lookup = {i: (src, tgt) for i, src, tgt in zip(indices, sources, targets)}

        result = []
        i = 0

        while i < len(s):
            if i in lookup:
                source, target = lookup[i]
                if s[i:i + len(source)] == source:
                    result.append(target)
                    i += len(source)
                    continue

            result.append(s[i])
            i += 1

        return ''.join(result)


class SolutionSortedReplacements:
    """Process in index order"""

    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        # Sort replacements by index
        ops = sorted(zip(indices, sources, targets))

        result = []
        prev = 0

        for idx, source, target in ops:
            # Add unchanged part
            result.append(s[prev:idx])

            # Check and apply replacement
            if s[idx:idx + len(source)] == source:
                result.append(target)
                prev = idx + len(source)
            else:
                prev = idx

        # Add remaining
        result.append(s[prev:])

        return ''.join(result)
