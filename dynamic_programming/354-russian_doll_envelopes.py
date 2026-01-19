#354. Russian Doll Envelopes
#Hard
#
#You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
#represents the width and the height of an envelope.
#
#One envelope can fit into another if and only if both the width and height of
#one envelope are greater than the other envelope's width and height.
#
#Return the maximum number of envelopes you can Russian doll (i.e., put one
#inside the other).
#
#Note: You cannot rotate an envelope.
#
#Example 1:
#Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
#Output: 3
#Explanation: The maximum number of envelopes you can Russian doll is 3
#([2,3] => [5,4] => [6,7]).
#
#Example 2:
#Input: envelopes = [[1,1],[1,1],[1,1]]
#Output: 1
#
#Constraints:
#    1 <= envelopes.length <= 10^5
#    envelopes[i].length == 2
#    1 <= wi, hi <= 10^5

import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width ascending, then by height descending
        # This way, for same width, we won't pick multiple envelopes
        # Then find LIS on heights

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # LIS using binary search
        dp = []  # dp[i] = smallest ending element of LIS of length i+1

        for _, h in envelopes:
            pos = bisect.bisect_left(dp, h)
            if pos == len(dp):
                dp.append(h)
            else:
                dp[pos] = h

        return len(dp)

    # Standard DP approach O(n^2) - TLE for large inputs
    def maxEnvelopesDP(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
