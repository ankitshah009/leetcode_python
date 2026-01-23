#1989. Maximum Number of People That Can Be Caught in Tag
#Medium
#
#You are playing a game of tag with your friends. In tag, people are divided
#into two teams: people who are "it" (the taggers), and people who are not
#"it" (the runners). The taggers want to catch as many runners as possible.
#
#You are given a 0-indexed integer array team containing only zeros (for
#runners) and ones (for taggers), where team[i] = 1 means that player i is a
#tagger. You are also given an integer dist.
#
#A tagger at index i can catch a runner at index j if dist >= |i - j|. Each
#player can only be involved in one catch.
#
#Return the maximum number of catches that can be made.
#
#Example 1:
#Input: team = [0,1,0,1,0], dist = 3
#Output: 2
#Explanation: Tagger at 1 catches runner at 0, tagger at 3 catches runner at 2 or 4.
#
#Example 2:
#Input: team = [1], dist = 1
#Output: 0
#Explanation: No runners.
#
#Example 3:
#Input: team = [0], dist = 1
#Output: 0
#Explanation: No taggers.
#
#Constraints:
#    1 <= team.length <= 10^5
#    0 <= team[i] <= 1
#    1 <= dist <= team.length

from typing import List

class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        """
        Two pointer greedy: match taggers with nearest available runners.
        """
        n = len(team)
        taggers = [i for i in range(n) if team[i] == 1]
        runners = [i for i in range(n) if team[i] == 0]

        if not taggers or not runners:
            return 0

        catches = 0
        t, r = 0, 0  # Pointers for taggers and runners

        while t < len(taggers) and r < len(runners):
            tagger_pos = taggers[t]
            runner_pos = runners[r]

            if abs(tagger_pos - runner_pos) <= dist:
                # Can catch
                catches += 1
                t += 1
                r += 1
            elif runner_pos < tagger_pos:
                # Runner is too far left, skip this runner
                r += 1
            else:
                # Tagger is too far left, skip this tagger
                t += 1

        return catches


class SolutionSinglePass:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        """
        Single pass with two pointers.
        """
        n = len(team)
        catches = 0
        t = r = 0  # Tagger and runner indices (in team array)

        while t < n and r < n:
            # Find next tagger
            while t < n and team[t] == 0:
                t += 1
            # Find next runner
            while r < n and team[r] == 1:
                r += 1

            if t >= n or r >= n:
                break

            if abs(t - r) <= dist:
                catches += 1
                t += 1
                r += 1
            elif r < t:
                r += 1
            else:
                t += 1

        return catches


class SolutionBipartiteMatching:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        """
        Model as bipartite matching (conceptual, greedy is sufficient).
        """
        taggers = []
        runners = []

        for i, t in enumerate(team):
            if t == 1:
                taggers.append(i)
            else:
                runners.append(i)

        # Greedy matching
        catches = 0
        used_runners = set()

        for tagger in taggers:
            for runner in runners:
                if runner not in used_runners and abs(tagger - runner) <= dist:
                    catches += 1
                    used_runners.add(runner)
                    break

        return catches
