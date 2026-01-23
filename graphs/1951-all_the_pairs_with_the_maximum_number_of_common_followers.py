#1951. All the Pairs With the Maximum Number of Common Followers
#Medium
#
#Table: Relations
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| user_id     | int  |
#| follower_id | int  |
#+-------------+------+
#(user_id, follower_id) is the primary key for this table.
#Each row of this table indicates that user_id has a follower with id follower_id.
#
#Write an SQL query to find all the pairs of users with the maximum number of
#common followers. Return all pairs with user1_id < user2_id.
#
#This is a SQL problem. Below is a Python simulation approach.

from typing import List
from collections import defaultdict

class Solution:
    def maxCommonFollowersPairs(self, relations: List[List[int]]) -> List[List[int]]:
        """
        Find pairs of users with maximum common followers.
        """
        # Build user -> set of followers
        followers = defaultdict(set)

        for user_id, follower_id in relations:
            followers[user_id].add(follower_id)

        users = list(followers.keys())
        n = len(users)

        # Calculate common followers for each pair
        pair_common = {}

        for i in range(n):
            for j in range(i + 1, n):
                u1, u2 = users[i], users[j]
                if u1 > u2:
                    u1, u2 = u2, u1

                common = len(followers[users[i]] & followers[users[j]])
                pair_common[(u1, u2)] = common

        if not pair_common:
            return []

        # Find maximum common followers count
        max_common = max(pair_common.values())

        # Return all pairs with max common followers
        result = [[u1, u2] for (u1, u2), count in pair_common.items()
                  if count == max_common]

        return sorted(result)


# SQL Solution:
"""
WITH CommonFollowers AS (
    SELECT r1.user_id AS user1_id, r2.user_id AS user2_id, COUNT(*) AS common_count
    FROM Relations r1
    JOIN Relations r2 ON r1.follower_id = r2.follower_id AND r1.user_id < r2.user_id
    GROUP BY r1.user_id, r2.user_id
)
SELECT user1_id, user2_id
FROM CommonFollowers
WHERE common_count = (SELECT MAX(common_count) FROM CommonFollowers);
"""
