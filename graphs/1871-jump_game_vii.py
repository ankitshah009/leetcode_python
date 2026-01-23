#1871. Jump Game VII
#Medium
#
#You are given a 0-indexed binary string s and two integers minJump and
#maxJump. In the beginning, you are standing at index 0, which is equal to '0'.
#You can move from index i to index j if the following conditions are
#fulfilled:
#- i + minJump <= j <= min(i + maxJump, s.length - 1), and
#- s[j] == '0'.
#
#Return true if you can reach index s.length - 1 in s, or false otherwise.
#
#Example 1:
#Input: s = "011010", minJump = 2, maxJump = 3
#Output: true
#
#Example 2:
#Input: s = "01101110", minJump = 2, maxJump = 3
#Output: false
#
#Constraints:
#    2 <= s.length <= 10^5
#    s[i] is either '0' or '1'.
#    s[0] == '0'
#    1 <= minJump <= maxJump < s.length

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        BFS with range tracking to avoid revisiting.
        """
        n = len(s)
        if s[-1] == '1':
            return False

        reachable = [False] * n
        reachable[0] = True

        # furthest index we've processed jumps from
        furthest = 0

        for i in range(n):
            if not reachable[i]:
                continue

            # Jump range from i: [i + minJump, i + maxJump]
            start = max(i + minJump, furthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == '0':
                    reachable[j] = True

            furthest = max(furthest, i + maxJump)

        return reachable[-1]


class SolutionPrefixSum:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        DP with prefix sum for range query.
        """
        n = len(s)
        if s[-1] == '1':
            return False

        # dp[i] = can reach index i
        dp = [False] * n
        dp[0] = True

        # prefix[i] = number of reachable indices in [0, i)
        prefix = [0] * (n + 1)
        prefix[1] = 1

        for i in range(1, n):
            if s[i] == '0':
                # Check if any index in [i - maxJump, i - minJump] is reachable
                lo = max(0, i - maxJump)
                hi = i - minJump

                if hi >= 0 and prefix[hi + 1] - prefix[lo] > 0:
                    dp[i] = True

            prefix[i + 1] = prefix[i] + (1 if dp[i] else 0)

        return dp[-1]


class SolutionDeque:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        Sliding window with deque.
        """
        from collections import deque

        n = len(s)
        if s[-1] == '1':
            return False

        # Queue of reachable indices in the valid jump range
        queue = deque([0])
        furthest = 0

        for i in range(1, n):
            # Remove indices too far back
            while queue and queue[0] < i - maxJump:
                queue.popleft()

            # Check if i is reachable
            if s[i] == '0' and queue and queue[0] <= i - minJump:
                if i == n - 1:
                    return True
                queue.append(i)

        return False
