#1949. Strong Friendship
#Medium
#
#Table: Friendship
#+-------------+------+
#| Column Name | Type |
#+-------------+------+
#| user1_id    | int  |
#| user2_id    | int  |
#+-------------+------+
#(user1_id, user2_id) is the primary key for this table.
#Each row of this table indicates that the users user1_id and user2_id are
#friends.
#
#A friendship between a pair of friends x and y is strong if x and y have at
#least three common friends.
#
#Write an SQL query to find all the strong friendships.
#
#Note that the result table should not contain duplicates with user1_id <
#user2_id.
#
#This is a SQL problem. Below is a Python simulation approach.

from typing import List
from collections import defaultdict

class Solution:
    def strongFriendship(self, friendships: List[List[int]]) -> List[List[int]]:
        """
        Find pairs with at least 3 common friends.
        """
        # Build adjacency set
        friends = defaultdict(set)

        for u1, u2 in friendships:
            friends[u1].add(u2)
            friends[u2].add(u1)

        result = []

        # Check each friendship pair
        seen = set()
        for u1, u2 in friendships:
            # Ensure u1 < u2 to avoid duplicates
            if u1 > u2:
                u1, u2 = u2, u1

            if (u1, u2) in seen:
                continue
            seen.add((u1, u2))

            # Count common friends
            common = len(friends[u1] & friends[u2])

            if common >= 3:
                result.append([u1, u2])

        return result


# SQL Solution:
"""
WITH AllFriends AS (
    SELECT user1_id, user2_id FROM Friendship
    UNION ALL
    SELECT user2_id, user1_id FROM Friendship
)
SELECT f.user1_id, f.user2_id
FROM Friendship f
JOIN AllFriends a1 ON f.user1_id = a1.user1_id
JOIN AllFriends a2 ON f.user2_id = a2.user1_id AND a1.user2_id = a2.user2_id
GROUP BY f.user1_id, f.user2_id
HAVING COUNT(*) >= 3;
"""
