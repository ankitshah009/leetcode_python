#920. Number of Music Playlists
#Hard
#
#Your music player contains n different songs. You want to listen to goal songs
#during your trip. To avoid boredom, you will create a playlist so that:
#- Every song is played at least once.
#- A song can only be played again only if k other songs have been played.
#
#Return the number of possible playlists you can create. The answer may be very
#large, return it modulo 10^9 + 7.
#
#Example 1:
#Input: n = 3, goal = 3, k = 1
#Output: 6
#Explanation: Possible playlists are ABC, ACB, BAC, BCA, CAB, CBA.
#
#Example 2:
#Input: n = 2, goal = 3, k = 0
#Output: 6
#Explanation: AAB, ABA, ABB, BAA, BAB, BBA.
#
#Constraints:
#    0 <= k < n <= goal <= 100

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """
        DP where dp[i][j] = playlists of length i with j unique songs.
        """
        MOD = 10 ** 9 + 7

        # dp[i][j] = ways to create playlist of length i with j unique songs
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                # Add new song: j choices from remaining (n - j + 1) songs
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD

                # Replay old song: can replay if j > k
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD

        return dp[goal][n]


class SolutionMemo:
    """Memoization approach"""

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(length: int, unique: int) -> int:
            if length == 0:
                return 1 if unique == 0 else 0
            if unique > length or unique > n:
                return 0

            # Add new song
            result = dp(length - 1, unique - 1) * (n - unique + 1) % MOD

            # Replay old song
            if unique > k:
                result = (result + dp(length - 1, unique) * (unique - k)) % MOD

            return result

        return dp(goal, n)


class SolutionOptimized:
    """Space optimized DP"""

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, goal + 1):
            new_dp = [0] * (n + 1)
            for j in range(1, min(i, n) + 1):
                new_dp[j] = dp[j - 1] * (n - j + 1) % MOD
                if j > k:
                    new_dp[j] = (new_dp[j] + dp[j] * (j - k)) % MOD
            dp = new_dp

        return dp[n]
