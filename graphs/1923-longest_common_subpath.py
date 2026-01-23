#1923. Longest Common Subpath
#Hard
#
#There is a country of n cities numbered from 0 to n - 1. In this country,
#there is a road connecting every pair of cities.
#
#There are m friends numbered from 0 to m - 1 who are traveling through the
#country. Each one of them will take a path consisting of some cities. Each
#path is represented by an integer array that contains the visited cities in
#order. The path may contain a city more than once, but the same city will not
#be listed consecutively.
#
#Given an integer n and a 2D integer array paths where paths[i] is an integer
#array representing the path of the ith friend, return the length of the
#longest common subpath that is shared by every friend's path, or 0 if there is
#no common subpath at all.
#
#A subpath of a path is a contiguous sequence of cities within that path.
#
#Example 1:
#Input: n = 5, paths = [[0,1,2,3,4],
#                       [2,3,4],
#                       [4,0,1,2,3]]
#Output: 2
#Explanation: The longest common subpath is [2,3].
#
#Example 2:
#Input: n = 3, paths = [[0],[1],[2]]
#Output: 0
#
#Example 3:
#Input: n = 5, paths = [[0,1,2,3,4],
#                       [4,3,2,1,0]]
#Output: 1
#
#Constraints:
#    1 <= n <= 10^5
#    m == paths.length
#    2 <= m <= 10^5
#    sum(paths[i].length) <= 10^5
#    0 <= paths[i][j] < n
#    The same city is not listed multiple times consecutively in paths[i].

from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        """
        Binary search on length + rolling hash.
        """
        def has_common_subpath(length: int) -> bool:
            """Check if there's a common subpath of given length."""
            if length == 0:
                return True

            BASE = n + 1
            MOD = (1 << 61) - 1  # Large prime for hash

            # Precompute BASE^(length-1) % MOD
            power = pow(BASE, length - 1, MOD)

            # Find all hashes of length-subpaths for first path
            common_hashes = None

            for path in paths:
                if len(path) < length:
                    return False

                path_hashes = set()
                h = 0

                # Initial hash
                for i in range(length):
                    h = (h * BASE + path[i]) % MOD

                path_hashes.add(h)

                # Rolling hash
                for i in range(length, len(path)):
                    h = ((h - path[i - length] * power) * BASE + path[i]) % MOD
                    path_hashes.add(h)

                if common_hashes is None:
                    common_hashes = path_hashes
                else:
                    common_hashes &= path_hashes

                if not common_hashes:
                    return False

            return bool(common_hashes)

        # Binary search
        min_len = min(len(p) for p in paths)
        lo, hi = 0, min_len

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if has_common_subpath(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo


class SolutionDoubleHash:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        """
        Double hashing to reduce collision probability.
        """
        def check(length: int) -> bool:
            if length == 0:
                return True

            BASE1, MOD1 = n + 1, (1 << 61) - 1
            BASE2, MOD2 = n + 7, (1 << 60) - 1

            pow1 = pow(BASE1, length - 1, MOD1)
            pow2 = pow(BASE2, length - 1, MOD2)

            common = None

            for path in paths:
                if len(path) < length:
                    return False

                hashes = set()
                h1, h2 = 0, 0

                for i in range(length):
                    h1 = (h1 * BASE1 + path[i]) % MOD1
                    h2 = (h2 * BASE2 + path[i]) % MOD2

                hashes.add((h1, h2))

                for i in range(length, len(path)):
                    h1 = ((h1 - path[i-length] * pow1) * BASE1 + path[i]) % MOD1
                    h2 = ((h2 - path[i-length] * pow2) * BASE2 + path[i]) % MOD2
                    hashes.add((h1, h2))

                common = hashes if common is None else common & hashes
                if not common:
                    return False

            return bool(common)

        lo, hi = 0, min(len(p) for p in paths)

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
