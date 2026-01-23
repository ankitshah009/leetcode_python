#1125. Smallest Sufficient Team
#Hard
#
#In a project, you have a list of required skills req_skills, and a list of
#people. The ith person people[i] contains a list of skills that the person has.
#
#Consider a sufficient team: a set of people such that for every required
#skill in req_skills, there is at least one person in the team who has that
#skill. We can represent these teams by the index of each person.
#
#For example, team = [0, 1, 3] represents the people with skills people[0],
#people[1], and people[3].
#
#Return any sufficient team of the smallest possible size, represented by
#the index of each person. You may return the answer in any order.
#
#It is guaranteed an answer exists.
#
#Example 1:
#Input: req_skills = ["java","nodejs","reactjs"],
#       people = [["java"],["nodejs"],["nodejs","reactjs"]]
#Output: [0,2]
#
#Example 2:
#Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"],
#       people = [["algorithms","math","java"],["algorithms","math","reactjs"],
#                ["java","csharp","aws"],["reactjs","csharp"],
#                ["csharp","math"],["aws","java"]]
#Output: [1,2]
#
#Constraints:
#    1 <= req_skills.length <= 16
#    1 <= req_skills[i].length <= 16
#    req_skills[i] consists of lowercase English letters.
#    All the strings of req_skills are unique.
#    1 <= people.length <= 60
#    0 <= people[i].length <= 16
#    1 <= people[i][j].length <= 16
#    people[i][j] consists of lowercase English letters.
#    All the strings of people[i] are unique.
#    Every skill in people[i] is a skill in req_skills.
#    It is guaranteed a sufficient team exists.

from typing import List
from functools import lru_cache

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """
        Bitmask DP: State is which skills are covered.
        dp[mask] = smallest team to cover skills in mask.
        """
        n = len(req_skills)
        m = len(people)

        # Map skills to indices
        skill_idx = {skill: i for i, skill in enumerate(req_skills)}

        # Convert each person's skills to bitmask
        person_masks = []
        for person in people:
            mask = 0
            for skill in person:
                mask |= (1 << skill_idx[skill])
            person_masks.append(mask)

        # DP: dp[mask] = list of person indices
        target = (1 << n) - 1
        dp = {0: []}

        for i, mask in enumerate(person_masks):
            for covered, team in list(dp.items()):
                new_covered = covered | mask
                if new_covered not in dp or len(dp[new_covered]) > len(team) + 1:
                    dp[new_covered] = team + [i]

        return dp[target]


class SolutionMemo:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """Memoized recursion"""
        n = len(req_skills)
        skill_idx = {s: i for i, s in enumerate(req_skills)}

        person_masks = []
        for person in people:
            mask = sum(1 << skill_idx[s] for s in person)
            person_masks.append(mask)

        target = (1 << n) - 1

        @lru_cache(maxsize=None)
        def dp(mask, idx):
            if mask == target:
                return []
            if idx == len(people):
                return None

            # Skip this person
            result = dp(mask, idx + 1)

            # Include this person
            new_mask = mask | person_masks[idx]
            with_person = dp(new_mask, idx + 1)

            if with_person is not None:
                candidate = [idx] + with_person
                if result is None or len(candidate) < len(result):
                    result = candidate

            return result

        return dp(0, 0)
