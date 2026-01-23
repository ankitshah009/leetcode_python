#1079. Letter Tile Possibilities
#Medium
#
#You have n tiles, where each tile has one letter tiles[i] printed on it.
#
#Return the number of possible non-empty sequences of letters you can make
#using the letters printed on those tiles.
#
#Example 1:
#Input: tiles = "AAB"
#Output: 8
#Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
#"ABA", "BAA".
#
#Example 2:
#Input: tiles = "AAABBC"
#Output: 188
#
#Example 3:
#Input: tiles = "V"
#Output: 1
#
#Constraints:
#    1 <= tiles.length <= 7
#    tiles consists of uppercase English letters.

from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Backtracking: Count permutations of all subsets.
        Use counter to handle duplicates.
        """
        count = Counter(tiles)
        result = 0

        def backtrack():
            nonlocal result
            for c in count:
                if count[c] > 0:
                    result += 1
                    count[c] -= 1
                    backtrack()
                    count[c] += 1

        backtrack()
        return result


class SolutionMath:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Mathematical approach: Sum of permutations for each subset size.
        P(n, k) / product of factorials of duplicate counts.
        """
        from math import factorial

        count = Counter(tiles)
        counts = list(count.values())
        n = len(tiles)

        def count_permutations(remaining, subset_counts):
            if sum(subset_counts) == 0:
                return 0

            # Count permutations with these counts
            total = sum(subset_counts)
            result = factorial(total)
            for c in subset_counts:
                result //= factorial(c)

            # Add permutations of smaller subsets
            for i in range(len(subset_counts)):
                if subset_counts[i] > 0:
                    subset_counts[i] -= 1
                    result += count_permutations(remaining - 1, subset_counts)
                    subset_counts[i] += 1

            return result

        return count_permutations(n, counts)


class SolutionSet:
    def numTilePossibilities(self, tiles: str) -> int:
        """Generate all permutations and use set to dedupe"""
        from itertools import permutations

        result = set()
        for length in range(1, len(tiles) + 1):
            for perm in permutations(tiles, length):
                result.add(perm)

        return len(result)
