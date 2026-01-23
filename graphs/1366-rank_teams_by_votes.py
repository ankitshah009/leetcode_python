#1366. Rank Teams by Votes
#Medium
#
#In a special ranking system, each voter gives a rank from highest to lowest
#to all teams participated in the competition.
#
#The ordering of teams is decided by who received the most position-one votes.
#If two or more teams tie in the first position, we consider the second position
#to resolve the conflict, if they tie again, we continue this process until the
#ties are resolved. If two or more teams are still tied after considering all
#positions, we rank them alphabetically based on their team letter.
#
#Given an array of strings votes which is the votes of all voters in the ranking
#systems. Sort all teams according to the ranking system described above.
#
#Return a string of all teams sorted by the ranking system.
#
#Example 1:
#Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
#Output: "ACB"
#Explanation: Team A was ranked first place by 5 voters. No other team was voted as first place so team A is the first team.
#Team B was ranked second by 2 voters and was ranked third by 3 voters.
#Team C was ranked second by 3 voters and was ranked third by 2 voters.
#As most voters ranked C second, team C is the second team and team B is the third.
#
#Example 2:
#Input: votes = ["WXYZ","XYZW"]
#Output: "XWYZ"
#
#Example 3:
#Input: votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
#Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"
#
#Constraints:
#    1 <= votes.length <= 1000
#    1 <= votes[i].length <= 26
#    votes[i].length == votes[j].length for 0 <= i, j < votes.length.
#    votes[i][j] is an English uppercase letter.
#    All characters of votes[i] are unique.
#    All the characters that occur in votes[0] also occur in votes[j] where 1 <= j < votes.length.

from typing import List
from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """
        Count position votes for each team.
        Sort by (position votes tuple descending, team letter ascending).
        """
        if len(votes) == 1:
            return votes[0]

        n = len(votes[0])
        teams = list(votes[0])

        # Count votes at each position for each team
        count = defaultdict(lambda: [0] * n)

        for vote in votes:
            for pos, team in enumerate(vote):
                count[team][pos] += 1

        # Sort: by position votes (descending), then alphabetically
        teams.sort(key=lambda t: ([-c for c in count[t]], t))

        return ''.join(teams)


class SolutionExplicit:
    def rankTeams(self, votes: List[str]) -> str:
        """More explicit implementation"""
        num_positions = len(votes[0])
        teams = set(votes[0])

        # Initialize vote counts
        vote_count = {team: [0] * num_positions for team in teams}

        # Count votes
        for vote in votes:
            for pos, team in enumerate(vote):
                vote_count[team][pos] += 1

        # Create sorting key
        def sort_key(team):
            # Negate counts for descending order, then team name for tiebreaker
            return ([-c for c in vote_count[team]], team)

        return ''.join(sorted(teams, key=sort_key))
