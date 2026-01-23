#649. Dota2 Senate
#Medium
#
#In the world of Dota2, there are two parties: the Radiant and the Dire.
#
#The Dota2 senate consists of senators coming from two parties. Now the Senate
#wants to decide on a change in the Dota2 game. The voting for this change is a
#round-based procedure. In each round, each senator can exercise one of the two rights:
#
#- Ban one senator's right: A senator can make another senator lose all his rights
#  in this and all the following rounds.
#- Announce the victory: If this senator found the senators who still have rights
#  to vote are all from the same party, he can announce the victory and decide on
#  the change in the game.
#
#Given a string senate representing each senator's party belonging. The character
#'R' and 'D' represent the Radiant party and the Dire party. Then if there are n
#senators, the size of the given string will be n.
#
#The round-based procedure starts from the first senator to the last senator in
#the given order. This procedure will last until the end of voting.
#
#Assuming each senator is smart enough and will play the best strategy for their party,
#predict which party will finally announce the victory and change the Dota2 game.
#Return "Radiant" or "Dire".
#
#Example 1:
#Input: senate = "RD"
#Output: "Radiant"
#
#Example 2:
#Input: senate = "RDD"
#Output: "Dire"
#
#Constraints:
#    n == senate.length
#    1 <= n <= 10^4
#    senate[i] is either 'R' or 'D'.

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """
        Greedy simulation using two queues.
        Each senator bans the next opponent.
        """
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, c in enumerate(senate):
            if c == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            # Senator with smaller index acts first and bans the other
            if r < d:
                radiant.append(r + n)  # Add back with larger index for next round
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"


class SolutionSimulation:
    """Direct simulation"""

    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        ban_r = ban_d = 0

        while True:
            new_senate = []

            for c in senate:
                if c == 'R':
                    if ban_r > 0:
                        ban_r -= 1
                    else:
                        ban_d += 1
                        new_senate.append('R')
                else:
                    if ban_d > 0:
                        ban_d -= 1
                    else:
                        ban_r += 1
                        new_senate.append('D')

            if not new_senate or new_senate == senate:
                break
            senate = new_senate

        return "Radiant" if 'R' in senate else "Dire"
