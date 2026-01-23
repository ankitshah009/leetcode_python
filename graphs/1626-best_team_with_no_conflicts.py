#1626. Best Team With No Conflicts
#Medium
#
#You are the manager of a basketball team. For the upcoming tournament, you want
#to choose the team with the highest overall score. The score of the team is the
#sum of scores of all the players in the team.
#
#However, the basketball team is not allowed to have conflicts. A conflict exists
#if a younger player has a strictly higher score than an older player. A conflict
#does not occur between players of the same age.
#
#Given two lists, scores and ages, where each scores[i] and ages[i] represents
#the score and age of the ith player, respectively, return the highest overall
#score of all possible basketball teams.
#
#Example 1:
#Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
#Output: 34
#Explanation: You can choose all the players.
#
#Example 2:
#Input: scores = [4,5,6,5], ages = [2,1,2,1]
#Output: 16
#Explanation: Choose players with ages 2 and score 4, 6 and player with age 1
#and score 5. The team's total score is 4 + 5 + 6 + 5 = 16 + 4 = 20... Actually
#best is [5,5,6] = 16 without conflicts.
#
#Example 3:
#Input: scores = [1,2,3,5], ages = [8,9,10,1]
#Output: 6
#Explanation: Choose players with age 8, 9, 10 with scores 1+2+3=6.
#
#Constraints:
#    1 <= scores.length, ages.length <= 1000
#    scores.length == ages.length
#    1 <= scores[i] <= 10^6
#    1 <= ages[i] <= 1000

from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        Sort by age (then by score for same age).
        Then find longest increasing subsequence by score with max sum.

        After sorting, if we pick players in order, older players come later.
        For no conflict, we need non-decreasing scores.
        """
        n = len(scores)
        players = sorted(zip(ages, scores))

        # dp[i] = max score achievable ending with player i
        dp = [0] * n

        for i in range(n):
            dp[i] = players[i][1]  # At minimum, just this player

            for j in range(i):
                # Can include player j before player i if score[j] <= score[i]
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)


class SolutionBIT:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        Optimized with Binary Indexed Tree for range max query.
        """
        n = len(scores)
        players = sorted(zip(ages, scores))

        # Coordinate compress scores
        unique_scores = sorted(set(scores))
        score_to_idx = {s: i + 1 for i, s in enumerate(unique_scores)}
        m = len(unique_scores)

        # BIT for range max
        bit = [0] * (m + 1)

        def update(idx, val):
            while idx <= m:
                bit[idx] = max(bit[idx], val)
                idx += idx & (-idx)

        def query(idx):
            result = 0
            while idx > 0:
                result = max(result, bit[idx])
                idx -= idx & (-idx)
            return result

        result = 0

        for age, score in players:
            idx = score_to_idx[score]
            # Max score for scores <= current score
            prev_max = query(idx)
            curr = prev_max + score
            result = max(result, curr)
            update(idx, curr)

        return result


class SolutionDetailed:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        Detailed DP solution with explanation.

        After sorting by (age, score), the problem becomes:
        Select a subsequence where scores are non-decreasing.
        Maximize sum of selected scores.

        This is similar to Longest Increasing Subsequence but maximizing sum.
        """
        n = len(scores)

        # Pair and sort: primary by age, secondary by score
        # This ensures older players come after younger
        # For same age, sort by score (no conflict within same age)
        players = sorted(zip(ages, scores), key=lambda x: (x[0], x[1]))

        # dp[i] = max team score using players up to i, with player i included
        dp = [0] * n

        for i in range(n):
            age_i, score_i = players[i]
            dp[i] = score_i  # Just player i alone

            for j in range(i):
                age_j, score_j = players[j]
                # Player j is younger or same age (due to sorting)
                # No conflict if score_j <= score_i
                if score_j <= score_i:
                    dp[i] = max(dp[i], dp[j] + score_i)

        return max(dp)
