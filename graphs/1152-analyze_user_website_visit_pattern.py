#1152. Analyze User Website Visit Pattern
#Medium
#
#You are given two string arrays username and website and an integer array
#timestamp. All the given arrays are of the same length and the tuple
#[username[i], website[i], timestamp[i]] indicates that the user username[i]
#visited the website website[i] at time timestamp[i].
#
#A pattern is a list of three websites (not necessarily distinct).
#
#For example, ["home", "away", "love"], ["hierarchical", "hierarchical", "hierarchical"],
#and ["hierarchical", "hierarchical", "hierarchical"] are all patterns.
#
#The score of a pattern is the number of users that visited all the websites
#in the pattern in the same order they appeared in the pattern.
#
#Return the pattern with the largest score. If there is more than one pattern
#with the same largest score, return the lexicographically smallest such pattern.
#
#Example 1:
#Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
#timestamp = [1,2,3,4,5,6,7,8,9,10],
#website = ["home","about","career","home","cart","maps","home","home","about","career"]
#Output: ["home","about","career"]
#
#Constraints:
#    3 <= username.length <= 50
#    1 <= username[i].length <= 10
#    timestamp.length == username.length
#    1 <= timestamp[i] <= 10^9
#    website.length == username.length
#    1 <= website[i].length <= 10

from typing import List
from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int],
                          website: List[str]) -> List[str]:
        """
        1. Group visits by user, sorted by time
        2. Generate all 3-sequences for each user
        3. Count unique users per pattern
        """
        # Group by user
        user_visits = defaultdict(list)
        for user, time, site in zip(username, timestamp, website):
            user_visits[user].append((time, site))

        # Sort each user's visits by time
        for user in user_visits:
            user_visits[user].sort()

        # Count patterns
        pattern_count = defaultdict(set)

        for user, visits in user_visits.items():
            sites = [site for _, site in visits]
            # Generate all 3-combinations (maintaining order)
            for combo in combinations(range(len(sites)), 3):
                pattern = (sites[combo[0]], sites[combo[1]], sites[combo[2]])
                pattern_count[pattern].add(user)

        # Find pattern with max users, lexicographically smallest if tie
        best_pattern = None
        best_count = 0

        for pattern, users in pattern_count.items():
            count = len(users)
            if count > best_count or (count == best_count and
                                       (best_pattern is None or pattern < best_pattern)):
                best_count = count
                best_pattern = pattern

        return list(best_pattern)


class SolutionAlternative:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int],
                          website: List[str]) -> List[str]:
        """More explicit approach"""
        # Combine and sort
        data = sorted(zip(timestamp, username, website))

        # Group by user
        user_sites = defaultdict(list)
        for _, user, site in data:
            user_sites[user].append(site)

        # Count patterns (use set for unique users)
        pattern_users = defaultdict(set)

        for user, sites in user_sites.items():
            n = len(sites)
            seen = set()
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        pattern = (sites[i], sites[j], sites[k])
                        if pattern not in seen:
                            seen.add(pattern)
                            pattern_users[pattern].add(user)

        # Find best
        result = min(pattern_users.keys(),
                    key=lambda p: (-len(pattern_users[p]), p))
        return list(result)
