#1583. Count Unhappy Friends
#Medium
#
#You are given a list of preferences for n friends, where n is always even.
#
#For each person i, preferences[i] contains a list of friends sorted in the order
#of preference. In other words, a friend earlier in the list is more preferred
#than a friend later in the list. Friends in each list are denoted by integers
#from 0 to n-1.
#
#All the friends are divided into pairs. The pairings are given in a list pairs,
#where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.
#
#However, this pairing may cause some of the friends to be unhappy. A friend x
#is unhappy if x is paired with y and there exists a friend u who is paired with
#v but:
#- x prefers u over y, and
#- u prefers x over v.
#
#Return the number of unhappy friends.
#
#Example 1:
#Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
#Output: 2
#Explanation:
#Friend 1 is unhappy because:
#- 1 is paired with 0 but prefers 3 over 0, and
#- 3 prefers 1 over 2.
#Friend 3 is unhappy because:
#- 3 is paired with 2 but prefers 1 over 2, and
#- 1 prefers 3 over 0.
#
#Example 2:
#Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
#Output: 0
#
#Example 3:
#Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
#Output: 4
#
#Constraints:
#    2 <= n <= 500
#    n is even.
#    preferences.length == n
#    preferences[i].length == n - 1
#    0 <= preferences[i][j] <= n - 1
#    preferences[i] does not contain i.
#    All values in preferences[i] are unique.
#    pairs.length == n/2
#    pairs[i].length == 2
#    xi != yi
#    0 <= xi, yi <= n - 1
#    Each person is contained in exactly one pair.

from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        Build preference rank map and check unhappy conditions.
        """
        # rank[x][y] = how much x prefers y (lower is better)
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for r, friend in enumerate(preferences[i]):
                rank[i][friend] = r

        # partner[x] = who x is paired with
        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        unhappy = 0

        for x in range(n):
            y = partner[x]

            # Check all friends u that x prefers over y
            for u in preferences[x]:
                if u == y:
                    break  # No more preferred friends

                v = partner[u]
                # Check if u prefers x over v
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break  # x is unhappy, no need to check more

        return unhappy


class SolutionDetailed:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        Detailed solution with comments.
        """
        # Build preference ranking for quick lookup
        # rank[i][j] = position of j in i's preference list
        rank = {}
        for i in range(n):
            rank[i] = {friend: idx for idx, friend in enumerate(preferences[i])}

        # Build partner mapping
        partner = {}
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        unhappy_count = 0

        for x in range(n):
            y = partner[x]  # x's current partner

            # Go through friends x prefers more than y
            for u in preferences[x]:
                if rank[x][u] >= rank[x][y]:
                    # u is not preferred over y
                    break

                # x prefers u over y
                v = partner[u]  # u's current partner

                # Check if u prefers x over v
                if rank[u][x] < rank[u][v]:
                    # Both conditions met: x is unhappy
                    unhappy_count += 1
                    break

        return unhappy_count


class SolutionSet:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        Using sets for preferred friends.
        """
        partner = {}
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        # For each person, set of friends preferred over partner
        preferred = {}
        for x in range(n):
            y = partner[x]
            pref_set = set()
            for friend in preferences[x]:
                if friend == y:
                    break
                pref_set.add(friend)
            preferred[x] = pref_set

        unhappy = 0
        for x in range(n):
            for u in preferred[x]:
                if x in preferred[u]:
                    unhappy += 1
                    break

        return unhappy
