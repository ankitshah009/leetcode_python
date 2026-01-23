#1733. Minimum Number of People to Teach
#Medium
#
#On a social network consisting of m users and some friendships between users,
#two users can communicate with each other if they know a common language.
#
#You are given an integer n, an array languages, and an array friendships where:
#- There are n languages numbered 1 through n.
#- languages[i] is the set of languages the ith user knows.
#- friendships[j] = [ui, vi] denotes a friendship between users ui and vi.
#
#You can choose one language and teach it to some users so that all friends can
#communicate with each other. Return the minimum number of users you need to
#teach.
#
#Note that friendships are not transitive, meaning if x is a friend of y and y
#is a friend of z, this doesn't guarantee that x is a friend of z.
#
#Example 1:
#Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
#Output: 1
#
#Example 2:
#Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
#Output: 2
#
#Constraints:
#    2 <= n <= 500
#    languages.length == m
#    1 <= m <= 500
#    1 <= languages[i].length <= n
#    1 <= languages[i][j] <= n
#    1 <= friendships.length <= 500
#    friendships[i].length == 2
#    1 <= ui < vi <= m

from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Find friendships that can't communicate, then find best language to teach.
        """
        # Convert to sets for O(1) lookup
        lang_sets = [set(langs) for langs in languages]

        # Find users who need to learn (have at least one non-communicating friend)
        users_to_teach = set()

        for u, v in friendships:
            u, v = u - 1, v - 1  # 0-indexed
            # Check if they share any language
            if not lang_sets[u] & lang_sets[v]:
                users_to_teach.add(u)
                users_to_teach.add(v)

        if not users_to_teach:
            return 0

        # For each language, count how many users already know it
        min_teach = len(users_to_teach)

        for lang in range(1, n + 1):
            # Count users who DON'T know this language
            need_teaching = sum(1 for user in users_to_teach
                              if lang not in lang_sets[user])
            min_teach = min(min_teach, need_teaching)

        return min_teach


class SolutionOptimized:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Same approach with slight optimization.
        """
        from collections import Counter

        lang_sets = [set(langs) for langs in languages]

        # Find users who can't communicate with at least one friend
        users_needing_common = set()
        for u, v in friendships:
            u, v = u - 1, v - 1
            if lang_sets[u].isdisjoint(lang_sets[v]):
                users_needing_common.add(u)
                users_needing_common.add(v)

        if not users_needing_common:
            return 0

        # Count languages known by users needing common language
        lang_count = Counter()
        for user in users_needing_common:
            for lang in lang_sets[user]:
                lang_count[lang] += 1

        # Best language is most commonly known among these users
        if lang_count:
            max_known = max(lang_count.values())
        else:
            max_known = 0

        return len(users_needing_common) - max_known
