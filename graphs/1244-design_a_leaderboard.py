#1244. Design A Leaderboard
#Medium
#
#Design a Leaderboard class, which has 3 functions:
#    addScore(playerId, score): Update the leaderboard by adding score to the
#    given player's score. If there is no player with such id in the leaderboard,
#    add him to the leaderboard with the given score.
#    top(K): Return the score sum of the top K players.
#    reset(playerId): Reset the score of the player with the given id to 0
#    (in other words erase it from the leaderboard). It is guaranteed that the
#    player was added to the leaderboard before calling this function.
#
#Initially, the leaderboard is empty.
#
#Example 1:
#Input:
#["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
#[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
#Output:
#[null,null,null,null,null,null,73,null,null,null,141]
#
#Constraints:
#    1 <= playerId, K <= 10000
#    It's guaranteed that K is less than or equal to the current number of players.
#    1 <= score <= 100
#    There will be at most 1000 function calls.

import heapq
from collections import defaultdict

class Leaderboard:
    """
    Simple approach: Store scores in dictionary.
    For top K, sort or use heap.
    """
    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        # Use heap to find top K
        return sum(heapq.nlargest(K, self.scores.values()))

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]


class LeaderboardSorted:
    """
    Using sorted container for efficient top K.
    """
    def __init__(self):
        from sortedcontainers import SortedList
        self.scores = {}  # playerId -> score
        self.sorted_scores = SortedList()  # Sorted list of scores

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scores:
            old_score = self.scores[playerId]
            self.sorted_scores.remove(old_score)
            self.scores[playerId] = old_score + score
        else:
            self.scores[playerId] = score

        self.sorted_scores.add(self.scores[playerId])

    def top(self, K: int) -> int:
        # Get top K from sorted list (last K elements)
        return sum(self.sorted_scores[-K:])

    def reset(self, playerId: int) -> None:
        old_score = self.scores[playerId]
        self.sorted_scores.remove(old_score)
        del self.scores[playerId]


class LeaderboardSimple:
    """Simplest implementation without external libraries"""
    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        sorted_scores = sorted(self.scores.values(), reverse=True)
        return sum(sorted_scores[:K])

    def reset(self, playerId: int) -> None:
        if playerId in self.scores:
            del self.scores[playerId]
