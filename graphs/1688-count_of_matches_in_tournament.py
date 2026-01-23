#1688. Count of Matches in Tournament
#Easy
#
#You are given an integer n, the number of teams in a tournament that has the
#following rules:
#- If the current number of teams is even, each team gets paired with another
#  team. A total of n / 2 matches are played, and n / 2 teams advance.
#- If the current number of teams is odd, one team randomly advances, and the
#  rest gets paired. A total of (n - 1) / 2 matches are played, and
#  (n - 1) / 2 + 1 teams advance.
#
#Return the number of matches played in the tournament until a winner is decided.
#
#Example 1:
#Input: n = 7
#Output: 6
#Explanation:
#- 1st Round: 7 teams, 3 matches, 4 advance.
#- 2nd Round: 4 teams, 2 matches, 2 advance.
#- 3rd Round: 2 teams, 1 match, 1 winner.
#Total = 3 + 2 + 1 = 6.
#
#Example 2:
#Input: n = 14
#Output: 13
#Explanation:
#- 1st Round: 14 teams, 7 matches, 7 advance.
#- 2nd Round: 7 teams, 3 matches, 4 advance.
#- 3rd Round: 4 teams, 2 matches, 2 advance.
#- 4th Round: 2 teams, 1 match, 1 winner.
#Total = 7 + 3 + 2 + 1 = 13.
#
#Constraints:
#    1 <= n <= 200

class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        Key insight: Each match eliminates exactly one team.
        To get 1 winner from n teams, need n-1 eliminations = n-1 matches.
        """
        return n - 1


class SolutionSimulation:
    def numberOfMatches(self, n: int) -> int:
        """
        Simulate the tournament.
        """
        matches = 0

        while n > 1:
            if n % 2 == 0:
                matches += n // 2
                n = n // 2
            else:
                matches += (n - 1) // 2
                n = (n - 1) // 2 + 1

        return matches


class SolutionRecursive:
    def numberOfMatches(self, n: int) -> int:
        """
        Recursive simulation.
        """
        if n == 1:
            return 0

        if n % 2 == 0:
            return n // 2 + self.numberOfMatches(n // 2)
        else:
            return (n - 1) // 2 + self.numberOfMatches((n - 1) // 2 + 1)


class SolutionProof:
    def numberOfMatches(self, n: int) -> int:
        """
        Mathematical proof:
        - Every match eliminates exactly 1 team
        - We need to eliminate n-1 teams to have 1 winner
        - Therefore, n-1 matches are needed
        """
        return n - 1


class SolutionIterative:
    def numberOfMatches(self, n: int) -> int:
        """
        Iterative approach with explicit rounds.
        """
        total = 0
        teams = n

        while teams > 1:
            games = teams // 2
            total += games
            teams = (teams + 1) // 2

        return total
